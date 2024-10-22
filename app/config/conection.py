from sqlalchemy import creat_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
#Paramentos da conexão com myql
db_usuario = "user"
db_passsword = "use_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

#URL de conexão para BD MySQL.
#DATABASE_URL = f"mysql+pymysql://usuario:senha@host:porta:nome_bd"
DATABASE_URL = f"mysql+pymysql://{db_usuario}:{db_passsword}@{db_host}:{db_port}/{db_name}"
#conectando ao banco de dados 
db= creat_engine(DATABASE_URL)
Session= sessionmaker(bind=db)
session = Session()

@contextmanager
def get_db():
    db = Session #Crindo uma sessão para ações no banco de dados.
    try:
        yield db # caso a sessão realize todas as tarefas, salva a operação 
        db.commit()
    except Exception as erro:
        db.rollback() #Desfaz todas alterações em caso de erro em alguma opereção
        raise erro  #Lança uma exception 
    finally:
        db.close() #Fecha conexão com banco de dados.
