print("\n\n---------------------------------------//---------------------------------------\n")
print("\nAtividade Prática: Sistema de uma Biblioteca\n")
print("Contexto:\n")
print("Você foi contratado para desenvolver um sistema de gerenciamento de biblioteca usando POO em Python.")
print("O sistema deve modelar livros, usuários e empréstimos, com funcionalidades básicas de cadastro, consulta e operações.")
print("\nRequisitos:\n")
print("- O sistema deve permitir o cadastro de livros, usuários e empréstimos.")
print("- O sistema deve permitir a consulta de livros cadastrados.")
print("- O sistema deve permitir a consulta de usuários cadastrados.")
print("\n---------------------------------------//---------------------------------------\n\n")
print("Desenvolvimentro\n")
print("\n---------------------------------------//---------------------------------------\n\n")

# DESAFIO (opcional) Classe LivroDigital:
# Herde de Livro e adicione o formato do e-book e formas de download.


class BibliotecaMeta(type):
    def __new__(cls, name, bases, dct):
        dct['usuarios'] = []
        dct['livros'] = []
        dct['emprestimos'] = []
        return super().__new__(cls, name, bases, dct)

class Biblioteca(metaclass=BibliotecaMeta):
    pass

''' ----------------------------------------início da classe Usuario---------------------------------------- '''

class Usuario(Biblioteca):
    def __init__(self, id_usuario, nome, email):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email

    def __repr__(self):
        return f"Usuário(id={self.id_usuario}, nome='{self.nome}')"

    def __add__(self, outro):
        if isinstance(outro, Usuario):
            Biblioteca.usuarios.append(outro)
        return self

    @staticmethod
    def consultar():
        if not Biblioteca.usuarios:
            print("Não há usuários cadastrados.")
            return

        print("\n--- Usuários Cadastrados ---")
        for usuario in Biblioteca.usuarios:
            print(f"ID: {usuario.id_usuario}, Nome: {usuario.nome}")

        id_consulta = input("Digite o ID do usuário que deseja consultar: ")
        usuario_encontrado = None
        for usuario in Biblioteca.usuarios:
            if usuario.id_usuario == id_consulta:
                usuario_encontrado = usuario
                break

        if usuario_encontrado:
            print("\n--- Dados do Usuário ---")
            print(f"   ID: {usuario_encontrado.id_usuario}")
            print(f" Nome: {usuario_encontrado.nome}")
            print(f"Email: {usuario_encontrado.email}")
        else:
            print(f"Usuário com ID '{id_consulta}' não encontrado.")

    @staticmethod
    def deletar():
        if not Biblioteca.usuarios:
            print("Não há usuários cadastrados para deletar.")
            return

        id_deletar = input("Digite o ID do usuário que deseja deletar: ")
        for i, usuario in enumerate(Biblioteca.usuarios):
            if usuario.id_usuario == id_deletar:
                del Biblioteca.usuarios[i]
                print(f"Usuário com ID '{id_deletar}' deletado com sucesso!")
                return
        print(f"Usuário com ID '{id_deletar}' não encontrado.")

    @staticmethod
    def cadastrar(id_usuario, nome, email):
        usuario = Usuario(id_usuario, nome, email)
        usuario + usuario  # Usando o método __add__ para adicionar à lista
        print(f"Usuário '{nome}' cadastrado com sucesso!")

''' ----------------------------------------final da classe Usuario---------------------------------------- '''



''' ----------------------------------------início da classe Livro---------------------------------------- '''

class Livro(Biblioteca):
    def __init__(self, id_livro, nome, editora, status="Disponível"):
        self.id_livro = id_livro
        self.nome = nome
        self.editora = editora
        self.status = status

    def __repr__(self):
        return f"Livro(id={self.id_livro}, nome='{self.nome}', status='{self.status}')"

    def __add__(self, outro):
        if isinstance(outro, Livro):
            Biblioteca.livros.append(outro)
        return self

    @staticmethod
    def cadastrar(id_livro, nome, editora):
        livro = Livro(id_livro, nome, editora)
        livro + livro # Usando o método __add__
        print(f"Livro '{nome}' cadastrado com sucesso!")

    @staticmethod
    def consultar():
        if not Biblioteca.livros:
            print("Não há livros cadastrados.")
            return

        print("\n--- Livros Cadastrados ---")
        for livro in Biblioteca.livros:
            print(f"ID: {livro.id_livro}, Nome: {livro.nome}")

        id_consulta = input("Digite o ID do livro que deseja consultar: ")
        livro_encontrado = None
        for livro in Biblioteca.livros:
            if livro.id_livro == id_consulta:
                livro_encontrado = livro
                break

        if livro_encontrado:
            print("\n--- Dados do Livro ---")
            print(f"     ID: {livro_encontrado.id_livro}")
            print(f"   Nome: {livro_encontrado.nome}")
            print(f"Editora: {livro_encontrado.editora}")
            print(f" Status: {livro_encontrado.status}")
        else:
            print(f"Livro com ID '{id_consulta}' não encontrado.")

    def mudar_status(self, novo_status):
        self.status = novo_status
        print(f"O status do livro '{self.nome}' (ID: {self.id_livro}) foi alterado para '{novo_status}'.")

''' ----------------------------------------final da classe Livro---------------------------------------- '''



''' -------------------------------------início da classe Emprestimo------------------------------------- '''

class Emprestimo(Usuario, Livro):
    @staticmethod
    def emprestar():
        if not Biblioteca.usuarios:
            print("Não há usuários cadastrados para realizar um empréstimo.")
            return
        if not Biblioteca.livros:
            print("Não há livros cadastrados para emprestar.")
            return

        print("\n--- Usuários Cadastrados ---")
        for usuario in Biblioteca.usuarios:
            print(f"ID: {usuario.id_usuario}, Nome: {usuario.nome}")

        id_usuario_emprestimo = input("Digite o ID do usuário que fará o empréstimo: ")
        usuario_emprestando = None
        for usuario in Biblioteca.usuarios:
            if usuario.id_usuario == id_usuario_emprestimo:
                usuario_emprestando = usuario
                break

        if not usuario_emprestando:
            print(f"Usuário com ID '{id_usuario_emprestimo}' não encontrado.")
            return

        livros_disponiveis = [livro for livro in Biblioteca.livros if livro.status == "Disponível"]
        if not livros_disponiveis:
            print("Não há livros disponíveis para empréstimo.")
            return

        print("\n--- Livros Disponíveis ---")
        for livro in livros_disponiveis:
            print(f"ID: {livro.id_livro}, Nome: {livro.nome}")

        id_livro_emprestimo = input("Digite o ID do livro a ser emprestado: ")
        livro_para_emprestar = None
        for livro in Biblioteca.livros:
            if livro.id_livro == id_livro_emprestimo:
                livro_para_emprestar = livro
                break

        if not livro_para_emprestar:
            print(f"Livro com ID '{id_livro_emprestimo}' não encontrado.")
            return
        if livro_para_emprestar.status == "Emprestado":
            print(f"O livro '{livro_para_emprestar.nome}' já está emprestado.")
            return

        Biblioteca.emprestimos.append({"usuario": usuario_emprestando, "livro": livro_para_emprestar})
        livro_para_emprestar.mudar_status("Emprestado")
        print(f"Empréstimo do livro '{livro_para_emprestar.nome}' para o usuário '{usuario_emprestando.nome}' realizado com sucesso!")

    @staticmethod
    def devolver():
        emprestimos_ativos = [emp for emp in Biblioteca.emprestimos if emp["livro"].status == "Emprestado"]

        if not emprestimos_ativos:
            print("Não há livros emprestados no momento.")
            return

        print("\n--- Livros Emprestados ---")
        for i, emprestimo in enumerate(emprestimos_ativos):
            print(f"{i+1}. ID: {emprestimo['livro'].id_livro}, Livro: {emprestimo['livro'].nome}, Usuário: {emprestimo['usuario'].nome}")

        try:
            opcao_devolucao = int(input("Digite o número do livro que será devolvido: "))
            if 1 <= opcao_devolucao <= len(emprestimos_ativos):
                livro_devolvido = emprestimos_ativos[opcao_devolucao - 1]["livro"]
                livro_devolvido.mudar_status("Disponível")
                # Remover o empréstimo da lista (opcional, dependendo da necessidade de histórico)
                for i, emp in enumerate(Biblioteca.emprestimos):
                    if emp["livro"] == livro_devolvido and emp["livro"].status == "Disponível":
                        del Biblioteca.emprestimos[i]
                        break
                print(f"Devolução do livro '{livro_devolvido.nome}' realizada com sucesso!")
            else:
                print("Opção inválida.")
        except ValueError:
            print("Por favor, digite um número.")

''' -------------------------------------final da classe Emprestimo------------------------------------- '''

# Função para exibir os créditos do sistema
def creditos():
    print("\n--- Sistema de Biblioteca ---\n")
    print("Desenvolvido por: Eduardo Luparele")
    print("Data: 11/05/2025\n")
    print("SENAC RIO - 2025")
    print("Curso: Programador Python Full Stack\n")
    print("Proposta de exercício referente a AULA 5 da UC3 - Programação Orientada a Objetos\n")
    print("\nMuita pesquisa e consultas no conteúdo de aula e ao Google\nforam feitas para desenvolver este sistema.\nToda a lógica foi compreendida e adaptada para o sistema.\n")

''' -------------------------------------início da interface do usuário------------------------------------- '''

if __name__ == "__main__":
    # Pré-definindo 5 usuários
    Usuario.cadastrar("1", "Ana Maria", "ana.maria@email.com")
    Usuario.cadastrar("2", "Pedro Silva", "pedro.silva@email.com")
    Usuario.cadastrar("3", "Carla Souza", "carla.souza@email.com")
    Usuario.cadastrar("4", "Lucas Oliveira", "lucas.oliveira@email.com")
    Usuario.cadastrar("5", "Mariana Costa", "mariana.costa@email.com")

    # Pré-definindo 5 livros
    Livro.cadastrar("1", "Dom Quixote", "Editora A")
    Livro.cadastrar("2", "Cem Anos de Solidão", "Editora B")
    Livro.cadastrar("3", "1984", "Editora C")
    Livro.cadastrar("4", "O Pequeno Príncipe", "Editora A")
    Livro.cadastrar("5", "Harry Potter e a Pedra Filosofal", "Editora D")

    while True:
        print("\n--- Menu da Biblioteca ---\n")
        print("1. Consultar Usuário")
        print("2. Deletar Usuário")
        print("3. Consultar Livro")
        print("4. Emprestar Livro")
        print("5. Devolver Livro")
        print("6. Créditos")
        print("0. Sair")

        opcao = input("\nDigite a opção desejada: ")

        if opcao == '1':
            print("\n--- Consultar Usuário ---")
            Usuario.consultar()
        elif opcao == '2':
            print("\n--- Deletar Usuário ---")
            Usuario.deletar()
        elif opcao == '3':
            print("\n--- Consultar Livro ---")
            Livro.consultar()
        elif opcao == '4':
            print("\n--- Emprestar Livro ---")
            Emprestimo.emprestar()
        elif opcao == '5':
            print("\n--- Devolver Livro ---")
            Emprestimo.devolver()
        elif opcao == '6':
            print("\n--- Créditos ---")
            creditos()
        elif opcao == '0':
            print("\nSaindo do sistema. Até logo!\n")
            break
        else:
            print("Vou ter que desenhar?... Tente novamente com uma opção válida.")

''' -------------------------------------final da interface do usuário------------------------------------- '''
# Fim do código