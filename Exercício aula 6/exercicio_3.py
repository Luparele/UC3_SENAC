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

# Exemplo de uso com os cadastros corretos:
if __name__ == "__main__":
    repositorio = UsuarioRepository()

    '''
    Cadastrando usuários para realizar testes
    '''
    repositorio.cadastrar({"nome": "Eduardo", "email": "eduardo@email.com"})
    repositorio.cadastrar({"nome": "Monique", "email": "monique@email.com"})
    repositorio.cadastrar({"nome": "Leticia", "email": "leticia@email.com"})

    ''' 
    Testando os métodos
    '''

    print("--- Teste: listar_todos() ---")
    todos_usuarios = repositorio.listar_todos()
    print("Todos os usuários:", todos_usuarios)

    print("\n--- Teste: buscar_por_email() ---")
    usuario_monique = repositorio.buscar_por_email("monique@email.com")
    print("Usuário com email monique@email.com:", usuario_monique)
    usuario_inexistente = repositorio.buscar_por_email("naoexiste@email.com")
    print("Usuário com email naoexiste@email.com:", usuario_inexistente)

    print("\n--- Teste: remover() ---")
    removido_eduardo = repositorio.remover("eduardo@email.com")
    print("Usuário eduardo@email.com removido:", removido_eduardo)
    print("Usuários após remoção:", repositorio.listar_todos())
    nao_removido = repositorio.remover("naoexiste@email.com")
    print("Tentativa de remover não existente:", nao_removido)

    print("\n--- Teste: atualizar() ---")
    atualizado = repositorio.atualizar({"nome": "Monique Atualizada", "email": "monique@email.com"})
    print("Atualização de monique@email.com:", atualizado)
    usuario_monique_atualizado = repositorio.buscar_por_email("monique@email.com")
    print("Usuário monique@email.com após atualização:", usuario_monique_atualizado)
    nao_atualizado = repositorio.atualizar({"nome": "Teste", "email": "naoexiste@email.com"})
    print("Tentativa de atualizar não existente:", nao_atualizado)

    print("\n--- Teste: listar_por_nome() ---")
    usuarios_eduardo = repositorio.listar_por_nome("Eduardo")
    print("Usuários com nome Eduardo:", usuarios_eduardo)
    usuarios_inexistente = repositorio.listar_por_nome("NomeInexistente")
    print("Usuários com nome NomeInexistente:", usuarios_inexistente)

    print("\n--- Teste: listar_por_email() ---")
    usuarios_com_email_leticia = repositorio.listar_por_email("leticia@email.com")
    print("Usuários com email leticia@email.com:", usuarios_com_email_leticia)
    usuarios_com_email_inexistente = repositorio.listar_por_email("outro@email.com")
    print("Usuários com email outro@email.com:", usuarios_com_email_inexistente)

    print("\n--- Teste: listar_por_nome_e_email() ---")
    usuario_leticia_completo = repositorio.listar_por_nome_e_email("Leticia", "leticia@email.com")
    print("Usuários com nome Leticia e email leticia@email.com:", usuario_leticia_completo)
    usuario_nao_encontrado = repositorio.listar_por_nome_e_email("Eduardo", "leticia@email.com")
    print("Usuários com nome Eduardo e email leticia@email.com:", usuario_nao_encontrado)