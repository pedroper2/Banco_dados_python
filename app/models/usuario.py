from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import declarative_base
from app.config.connection import db 

Base= declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True,autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150),unique=True) #Não aceita email repetido
    senha = Column(String(150))

    def __init__(self,nome:str,email:str,senha:str):
        self.nome = self._verificar_Geral(nome)
        self.email= self._verificar_Geral(email)
        self.senha = self._verificar_Geral(senha)

    def _verificar_Geral(self,true):
        if not isinstance(true,str):
            raise TypeError("Tipo inválido.")
        if not true.strip():
            raise ValueError("Insira um valor.")
        return true
#Criando tabela no banco de dados
Base.metadata.create_all(bind=db)