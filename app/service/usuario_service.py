from models.usuario import Usuario
from repositorios.usario_repositorio import UsuarioRepository
from app.test import tes_usario

class UsuarioService:
    def __init__(self,repository:UsuarioRepository):
        self.repository = repository

    def criar_usuario(self,nome:str,email:str,senha:str):
        try:
            usuario = Usuario(nome=nome,email=email,senha= senha)
            
            cadastro= self.repository.pesquisar_usario(usuario.email)

            if cadastro:
                print("Usuario já existe no banco de dados.")
                return 
            self.repository.salvar_usuario(usuario)
            print("Usuario salvo com sucesso!")

        except TypeError as erro: 
            print (f"Erro ao salva usuario:{erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.listar_todos_usuarios()
    
    def pesquisar_usuario(self):
        try:
            email_usuario= input("Digite o email do usuario: ")
            cadastro= self.repository.pesquisar_usario(email= email_usuario)
            if cadastro:
                print(F"Nome{cadastro.nome} email{cadastro.email} senha{cadastro.senha}")
                return
            else:
                print("Nome não encontrado")
            return
        except TypeError as error:
            print(f"Erro ao pesquisar o usuário: {error}")
        except Exception as error:
            print(f"Erro inesperado: {error}")
    
    def atualizar_dados_usuario(self):
        try:
            print(f"\nAtualizando dados do usuário.")

            email = input("Digite o e-mail do usuário: ") 
            cadastrado = self.repository.pesquisar_usuario_por_email(email)

            if cadastrado:
                cadastrado.nome = input("\nDigite um novo nome: ")
                cadastrado.email = input("\nDigite um novo e-mail: ")
                cadastrado.senha = input("\nDigite uma nova senha: ")
                self.repository.salvar_usuario(cadastrado)
                print("\nDados de usuário atualizados.")
            else:
                print("Usuário não encontrado.")
                return
        
        except TypeError as error:
            print(f"Erro ao atualizar o usuário: {error}")
        except Exception as error:
            print(f"Erro inesperado: {error}")
            
    def excluir_dados_usuario(self):
        try:
            print("\nExcluindo dados do usuário.")

            email = input("Digite o e-mail do usuário que será excluído: ")
            cadastrado = self.repository.pesquisar_usuario_por_email(email)

            if cadastrado:
                self.repository.excluir_usuario(cadastrado)
                print("\nUsuário excluído.")
            else:
                print("Usuário não encontrado.")
                return
        
        except TypeError as error:
            print(f"Erro ao excluir o usuário: {error}")
        except Exception as error:
            print(f"Erro inesperado: {error}")
        

        
