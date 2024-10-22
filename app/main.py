from app.service.usuario_service import UsuarioService
from repositorios.usario_repositorio import UsuarioRepository
from config.conection import Session
def main():
    session = Session ()
    repository = UsuarioRepository(session) 
    service = UsuarioService(repository)

    #criando um usuário.
    service.criar_usuario("Marta","marta12@gmail","123")

    #listando todos os usuarios.
    print ("\nlistando todos os usuarios.")
    lsita_usuarios = service.listar_todos_usuarios()
    for usuario in lsita_usuarios:
        print (f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

if __name__ == "__main__":
    main() 