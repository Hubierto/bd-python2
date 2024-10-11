from models.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)
            self.repository.salvar_usuario(usuario)
            print("Usuário salvo com sucesso!")
        except TypeError as erro:        
            print(f"Usuário salvo com sucesso: {erro}")
        except TypeError as erro:   
            print(f"Usuário salvo com sucesso: {erro}")
    
    def listar_todos_usuarios(self):    
        return self.repository.listar_todos_usuarios()
        
            

        