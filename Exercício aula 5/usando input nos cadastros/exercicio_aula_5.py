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

#DESAFIO NÃO FOI RESOLVIDO AINDA !!!    :(
# DESAFIO (opcional) Classe LivroDigital:
# Herde de Livro e adicione o formato do e-book e formas de download.


class BibliotecaMeta(type): 
    def __new__(cls, name, bases, dct): 
        
        dct['usuarios'] = [] # Inicializa uma lista para armazenar usuários na classe        
        dct['livros'] = [] # Inicializa uma lista para armazenar livros na classe
        dct['emprestimos'] = [] # Inicializa uma lista para armazenar empréstimos na classe
        return super().__new__(cls, name, bases, dct)# Cria a nova classe com os atributos modificados

class Biblioteca(metaclass=BibliotecaMeta): # Cria a classe usando a metaclasse BibliotecaMeta
    pass

''' ----------------------------------------início da classe Usuario---------------------------------------- '''

class Usuario(Biblioteca): # Cria a classe Usuario que herda de Biblioteca
    def __init__(self, id_usuario, nome, email): # Inicializa os atributos do usuário
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email

    def __repr__(self): # Representação técnica do usuário
        return f"Usuário(id={self.id_usuario}, nome='{self.nome}')"

    def __add__(self, outro): # Sobrecarga do operador + para adicionar usuários à lista
        if isinstance(outro, Usuario):
            Biblioteca.usuarios.append(outro)
        return self

    '''
    Método para consultar usuários
    1- Verifica se há usuários cadastrados
    2- Se não houver, informa ao usuário com uma mensagem
    3- Se houver, exibe os usuários cadastrados
    4- Solicita o ID do usuário a ser consultado
    5- Verifica se o ID existe na lista de usuários cadastrados
    6- Se existir, exibe os dados do usuário encontrado
    7- Se não existir, informa ao usuário que o ID não foi encontrado
    '''
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

    '''
    Método para deletar usuários
    1- Verifica se|houver, informa ao usuário com uma mensagem
    2- Se houver, solicita o ID do usuário a ser deletado
    3- Verifica se o ID existe na lista de usuários cadastrados
    4- Se existir, deleta o usuário da lista
    5- Se não existir, informa ao usuário que o ID não foi encontrado
    '''
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

    '''
    Método para cadastrar usuários
    1- Solicita o ID, nome e email do usuário
    2- Cria um novo usuário com os dados informados
    3- Adiciona o usuário à lista de usuários cadastrados
    4- Informa ao usuário que o usuário foi cadastrado com sucesso
    '''
    @staticmethod
    def cadastrar():
        id_usuario = input("Digite o ID do usuário: ")
        nome = input("Digite o nome do usuário: ").title()
        email = input("Digite o email do usuário: ")
        usuario = Usuario(id_usuario, nome, email)
        usuario + usuario  # Usando o método __add__ para adicionar à lista
        print(f"Usuário '{nome}' cadastrado com sucesso!")

''' ----------------------------------------final da classe Usuario---------------------------------------- '''



''' ----------------------------------------início da classe Livro---------------------------------------- '''
        
class Livro(Biblioteca):
    def __init__(self, id_livro, nome, editora, status="Disponível"): # Inicializa os atributos do livro
        self.id_livro = id_livro
        self.nome = nome
        self.editora = editora
        self.status = status

    def __repr__(self): # Representação técnica do livro
        return f"Livro(id={self.id_livro}, nome='{self.nome}', status='{self.status}')"

    def __add__(self, outro): # Sobrecarga do operador + para adicionar livros à lista
        if isinstance(outro, Livro):
            Biblioteca.livros.append(outro)
        return self

    '''
    Método para consultar livros
    1- Solicita o ID do livro a ser cadastrado
    2- Solicita o nome do livro a ser cadastrado, com formatação para título
    3- Solicita a editora do livro a ser cadastrado, com formatação para título
    4- Cria um novo livro com os dados informados
    5- Adiciona o livro à lista de livros cadastrados
    6- Informa ao usuário que o livro foi cadastrado com sucesso
    '''
    @staticmethod
    def cadastrar():
        id_livro = input("Digite o ID do livro: ")
        nome = input("Digite o nome do livro: ").title()
        editora = input("Digite a editora do livro: ").title()
        livro = Livro(id_livro, nome, editora)
        livro + livro # Usando o método __add__
        print(f"Livro '{nome}' cadastrado com sucesso!")

    '''
    Método para consultar livros
    1- Verifica se existem livros cadastrados, se não houver, informa ao usuário com uma mensagem
    2- Se houver, solicita o ID do livro a ser consultado
    3- Verifica se o ID existe na lista de livros cadastrados
    4- Se existir, imprime os dados do livro encontrado
    5- Se não existir, informa ao usuário que o ID não foi encontrado'''
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

    '''
    Método para alterar o status do livro
    1- faz a alteração do status do livro
    2- isso ocorre quando o método é chamado no método de empréstimo
    3- imprime uma mensagem informando que o status foi alterado
    '''
    def mudar_status(self, novo_status):
        self.status = novo_status
        print(f"O status do livro '{self.nome}' (ID: {self.id_livro}) foi alterado para '{novo_status}'.")
        
''' ----------------------------------------final da classe Livro---------------------------------------- '''



''' -------------------------------------início da classe Emprestimo------------------------------------- '''

class Emprestimo(Usuario, Livro):
    '''
    Método para emprestar livros
    1- Verifica se há usuários cadastrados, se não houver, informa ao usuário com uma mensagem
    2- Se houver, solicita o ID do usuário que fará o empréstimo
    3- Verifica se o ID existe na lista de usuários cadastrados
    4- Se existir, solicita o ID do livro a ser emprestado
    5- Verifica se o ID do livro existe na lista de livros cadastrados
    6- Se existir, verifica se o livro está disponível para empréstimo
    7- Se o livro estiver disponível, altera o status do livro para "Emprestado"
    8- Imprime uma mensagem informando que o livro foi emprestado com sucesso
    '''
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

    '''
    Método para devolver livros
    1- Verifica se existem empréstimos ativos, se não houver, informa ao usuário com uma mensagem
    2- Se houver, solicita o ID do livro a ser devolvido
    3- Verifica se o ID do livro existe na lista de empréstimos ativos
    4- Se existir, altera o status do livro para "Disponível"
    5- Imprime uma mensagem informando que o livro foi devolvido com sucesso
    '''
    @staticmethod
    def devolver():
        emprestimos_ativos = [emp for emp in Biblioteca.emprestimos if emp["livro"].status == "Emprestado"]

        if not emprestimos_ativos:
            print("Não há livros emprestados no momento.")
            return

        print("\n--- Livros Emprestados ---")
        for i, emprestimo in enumerate(emprestimos_ativos):
            print(f"{i+1}. ID: {emprestimo['livro'].id_livro}, Livro: {emprestimo['livro'].nome}, Usuário: {emprestimo['usuario'].nome}") # enumera os livros emprestados usando o método enumerate com uma contagem iniciando em 1.

        try:
            opcao_devolucao = int(input("Digite o número do livro que será devolvido: "))
            if 1 <= opcao_devolucao <= len(emprestimos_ativos):
                livro_devolvido = emprestimos_ativos[opcao_devolucao - 1]["livro"] # Subtrai 1 do número digitado pelo usuário para obter o índice correto na lista de empréstimos. mantendo sempre uma contagem iniciando em 1.
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

'''
Função principal do programa
1- Exibe um menu com opções para o usuário
2- Solicita a opção desejada pelo usuário
3- Executa a opção escolhida pelo usuário
4- Se a opção for inválida, informa ao usuário e solicita uma nova opção (com sarcasmo kkkk)
5- O loop continua até que o usuário escolha a opção de sair (0)
'''
if __name__ == "__main__":
    while True:
        print("\n--- Menu da Biblioteca ---\n")
        print("1. Cadastrar Usuário")
        print("2. Consultar Usuário")
        print("3. Deletar Usuário")
        print("4. Cadastrar Livro")
        print("5. Consultar Livro")
        print("6. Emprestar Livro")
        print("7. Devolver Livro")
        print("8. Créditos")
        print("0. Sair")

        opcao = input("\nDigite a opção desejada: ")

        if opcao == '1':
            print("\n--- Cadastrar Usuário ---")
            Usuario.cadastrar()
        elif opcao == '2':
            print("\n--- Consultar Usuário ---")
            Usuario.consultar()
        elif opcao == '3':
            print("\n--- Deletar Usuário ---")
            Usuario.deletar()
        elif opcao == '4':
            print("\n--- Cadastrar Livro ---")
            Livro.cadastrar()
        elif opcao == '5':
            print("\n--- Consultar Livro ---")
            Livro.consultar()
        elif opcao == '6':
            print("\n--- Emprestar Livro ---")
            Emprestimo.emprestar()
        elif opcao == '7':
            print("\n--- Devolver Livro ---")
            Emprestimo.devolver()
        elif opcao == '8':
            print("\n--- Créditos ---")
            creditos()
        elif opcao == '0':
            print("\nSaindo do sistema. Até logo!\n")
            break
        else:
            print("\nEssa opção não existe!\nVou ter que desenhar?...\nTente novamente com uma opção válida.\n")

''' -------------------------------------final da interface do usuário------------------------------------- '''
# Fim do código