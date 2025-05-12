# 3. Padrão de Acesso a Repositórios
# Crie uma classe UsuarioRepository com os seguintes métodos:

'''
- cadastrar(usuario): cadastra um usuário (dicionário com nome e email).
- listar_todos(): retorna uma lista com todos os usuários cadastrados.
- buscar_por_email(email): retorna o usuário correspondente ao email informado.
- remover(email): remove o usuário correspondente ao email informado. 
- atualizar(usuario): atualiza os dados do usuário correspondente ao email informado.
- listar_por_nome(nome): retorna uma lista com todos os usuários que possuem o nome informado.
- listar_por_email(email): retorna uma lista com todos os usuários que possuem o email informado.
- listar_por_nome_e_email(nome, email): retorna uma lista com todos os usuários que possuem o nome e email informados.
'''
class UsuarioRepository:
    def __init__(self):
        self.usuarios = []

    def cadastrar(self, usuario):
        """Cadastra um novo usuário."""
        if isinstance(usuario, dict) and "nome" in usuario and "email" in usuario:
            self.usuarios.append(usuario.copy())
        else:
            print("Erro: O usuário deve ser um dicionário com as chaves 'nome' e 'email'.")

    def listar_todos(self):
        """Retorna uma lista com todos os usuários cadastrados."""
        return list(self.usuarios)

    def buscar_por_email(self, email):
        """Retorna o usuário correspondente ao email informado."""
        for usuario in self.usuarios:
            if usuario.get("email") == email:
                return usuario
        return None

    def remover(self, email):
        """Remove o usuário correspondente ao email informado."""
        inicial_len = len(self.usuarios)
        self.usuarios = [usuario for usuario in self.usuarios if usuario.get("email") != email]
        return len(self.usuarios) < inicial_len

    def atualizar(self, usuario):
        """Atualiza os dados do usuário correspondente ao email informado."""
        for i, u in enumerate(self.usuarios):
            if u.get("email") == usuario.get("email"):
                self.usuarios[i] = usuario.copy()
                return True
        return False

    def listar_por_nome(self, nome):
        """Retorna uma lista com todos os usuários que possuem o nome informado."""
        return [usuario for usuario in self.usuarios if usuario.get("nome") == nome]

    def listar_por_email(self, email):
        """Retorna uma lista com todos os usuários que possuem o email informado."""
        return [usuario for usuario in self.usuarios if usuario.get("email") == email]

    def listar_por_nome_e_email(self, nome, email):
        """Retorna uma lista com todos os usuários que possuem o nome e email informados."""
        return [usuario for usuario in self.usuarios if usuario.get("nome") == nome and usuario.get("email") == email]

# Exemplo de uso:
if __name__ == "__main__":
    repositorio = UsuarioRepository()

    # Cadastrando usuários
    repositorio.cadastrar({"nome": "Alice", "email": "alice@example.com"})
    repositorio.cadastrar({"nome": "Bob", "email": "bob@example.com"})
    repositorio.cadastrar({"nome": "Alice", "email": "alice.second@example.com"})

    # Listar todos
    print("\n")
    print("Todos os usuários:", repositorio.listar_todos())
    print("\n")
    # Buscar por email
    usuario_bob = repositorio.buscar_por_email("bob@example.com")
    print("Usuário com email bob@example.com:", usuario_bob)
    print("\n")
    # Listar por nome
    usuarios_alice = repositorio.listar_por_nome("Alice")
    print("Usuários com nome Alice:", usuarios_alice)
    print("\n")
    # Listar por email (deve retornar uma lista, mesmo que haja apenas um)
    usuarios_com_email_alice = repositorio.listar_por_email("alice@example.com")
    print("Usuários com email alice@example.com:", usuarios_com_email_alice)
    print("\n")
    # Listar por nome e email
    usuarios_alice_second = repositorio.listar_por_nome_e_email("Alice", "alice.second@example.com")
    print("Usuários com nome Alice e email alice.second@example.com:", usuarios_alice_second)
    print("\n")
    # Atualizar usuário
    repositorio.atualizar({"nome": "Robert", "email": "bob@example.com"})
    print("Usuários após atualizar Bob:", repositorio.listar_todos())
    # Remover usuário
    removido = repositorio.remover("alice@example.com")
    print("\n")
    print("Usuário alice@example.com removido:", removido)
    print("\n")
    print("Usuários restantes:", repositorio.listar_todos())
    print("\n")