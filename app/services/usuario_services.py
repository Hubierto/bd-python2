from models.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            cadastrado = self.repository.pesquisar_usuario_por_email(email=usuario.email)

            if cadastrado:
                print("Usuário já cadastrado!")
                return
            
            self.repository.salvar_usuario(usuario)
            print("Usuário salvo com sucesso!")
        except TypeError as erro:        
            print(f"Erro ao cadastrar o usuário: {erro}")
        except TypeError as erro:   
            print(f"Ocorreu um erro inesperado: {erro}")
    
    def listar_todos_usuarios(self):    
        return self.repository.listar_todos_usuarios()
        
            

        