from models.usario import Usuario
from sqlalchemy.orm import Session 
from models import usario
class UsuarioRepository:
    def __init__(self,session:Session) -> None:
        self.session = session

    def salvar_usuario(self,usuario:Usuario):
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh()
    def pesquisa_usario(self,email:str):
        return self.session.query(Usuario).filter_by(email = email).first()
    
    def excluir_usuario(self,usuario:Usuario):
        self.session.delete(usuario)
        self.session.commit()
        self.session.refresh()

    def listar_todos_usuarios(self):
        return self.session.query (Usuario).all()
        