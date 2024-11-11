import os 
import sys


sys.path.append (os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from app.config.connection import Session
from app.repositorios.usario_repositorio import UsuarioRepository
from app.service.usuario_service import UsuarioService


def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    #Solicitando dados para o usuário.

    while True:
        print("1 - Adicionar usuário.")
        print("2 - Pesquisar um usuário.")
        print("3 - Atualizar dados de um usuário.")
        print("4 - Excluir um usuário.")
        print("5 - Exibir todos os usuários cadastrados.")
        print("0 - Sair.")
    
        
        resposta = (input("Informe o código desejado: "))
        os.system("cls || clear")
        
        match(resposta):
            case '1':
                print("\nAdicionando usuário.")
                nome = input("Digite seu nome: ")
                email = input("Digite seu email: ")
                senha = input("Digite sua senha: ")

                service.criar_usuario(nome=nome,email=email,senha=senha)
            case '2':
                service.pesquisar_usuario()
            case '3':
                service.atualizar_dados_usuario()
            case '4':
                service.excluir_dados_usuario()
            case '5':
                print("\nListando todos os usuários cadastrados.")
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(f"Nome: {usuario.nome} - E-mail: {usuario.email} - Senha: {usuario.senha}")
            case '0':    
                break
            case _:
                print("Código inválido, tente novamente.")            

    session.close()
if __name__ == "__main__":
    os.system("cls || clear")
    main()
    
            

              
              
            