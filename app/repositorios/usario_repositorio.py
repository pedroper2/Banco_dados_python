from app.models.usuario import Usuario
from sqlalchemy.orm import Session 


class UsuarioRepository:
    def __init__(self,session:Session):
        self.session = session

    def salvar_usuario(self,usuario:Usuario):
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)

    def pesquisa_usario(self,nome:str):
        return self.session.query(Usuario).filter_by(nome= nome).first()
    
    def excluir_usuario(self,usuario:Usuario):
        self.session.delete(usuario)
        self.session.commit()
        self.session.refresh(usuario)

    def listar_todos_usuarios(self):
        return self.session.query (Usuario).all()

        