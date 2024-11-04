import os
from sqlalchemy import create_engine, Column,String,Integer
from sqlalchemy.orm import sessionmaker,declarative_base
#from app.service.usuario_service import UsuarioService
#from repositorios.usario_repositorio import UsuarioRepository
from config.conection import Session
#Criando banco de dados
MEU_BANCO= create_engine (("sqlite:///meubanco.db"))

# Criando conexão com banco de dados.
Session = sessionmaker(bind= MEU_BANCO)
session = Session()
# Criando tabela.
Base = declarative_base()
os.system("clear || cls")
# Definindo campos da tabela.
class Usuario(Base):
    __tablename__ = "usuarios"
    id= Column("id",Integer,primary_key=True,autoincrement= True)
    nome= Column("nome",String)
    email= Column("email",String)
    senha= Column("senha",String)
# Criando tabelas no banco de dados.
Base.metadata.create_all(bind= MEU_BANCO)
os.system("clear || cls")
 # Definindo atributos da classe.
def __init__(self,nome:str,email:str,senha:str):
    self.nome= nome
    self.email= email
    self.senha= senha
def create_usuario():
            inserir_nome = input("Digite seu nome: ")
            inserir_email = input("Digite seu e-mail: ")
            inserir_senha = input("Digite sua senha: ")
            usuario = Usuario(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
            session.add(usuario)
            session.commit()
            return create_usuario 
def exibir_todos_usuarios():
    lista_usuarios= session.query(Usuario).all()
    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")
        return exibir_todos_usuarios
    
def pesquisa_usuario():
    nome_usuario= input ("Digite o nome do usuario: ")
    usuario = session.query (Usuario).filter_by(nome= nome_usuario).first()
    if usuario:
        print (f"\n{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")
    else:
        print("Usuario não encontradiodfksadojk")
        return pesquisa_usuario
def altera_dados():
    nome_usuario= input ("Digite o nome do usuario que sera atualizado:")
    usuario = session.query (Usuario).filter_by(nome= nome_usuario).first()
    if usuario:
        usuario.nome = input("Digite seu nome: ")
        usuario.email =input ("Digite seu email: ")
        usuario.senha =input ("Digite sua senha: ")
        session.commit() 
    else:
        print("usuario não encontrado")
        return altera_dados
    
def delete_usuario():
    nome_usuario= input ("Digite o nome do usuario que sera excluido:")
    usuario = session.query (Usuario).filter_by(nome= nome_usuario).first()
    if usuario:
         session.delete(usuario)
         session.commit()
         print("\ndeletando usuario")     

def menu ():
    print(f"\n1-Adiciona usario"
          f"\n2-Pesquisa usuario"
          f"\n3- Atualizar dados de usuario"
          f"\n4-Excluir um usuario"
          f"\n5- Exibir todos os usuarios"
          f"\n0- sair")
while True:
    menu()
    opcao= input("Digite uma opcao: ")
    os.system("clear || cls")
    match(opcao):
        case '1':
            print(f"Criando um usuario: ")
            print("Solicitando dados para o usuário. ")
            create_usuario()
        case '2':
            print("Dados do usuario:")
            pesquisa_usuario()
        case '3':
            print("mudando os dados do usuario")
            altera_dados()
        case '4':
            print("Deletando usuario: ")
            delete_usuario()
        case '5':
            print("Exibindo todos os usuarios: ")
            exibir_todos_usuarios()
        case '0':
            print("fim")
            break
        case _:
            print("opção invalida")
            os.system ("clear || cls")
            

              
              
            