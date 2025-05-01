#Implemente um sistema de gerenciamento de tarefas (to-do list) em memória usando dicionários e JSON.

#Use um dicionário para armazenar tarefas no formato exemplificado abaixo:
'''
tarefas = {
    1: {"titulo": "Estudar Python", "status": "pendente"},
    2: {"titulo": "Fazer relatório", "status": "concluído"}
}
'''
#Implemente os recursos abaixo:
'''
listar_tarefas(): Retorna todas as tarefas em JSON.

adicionar_tarefa(id, titulo, status): Adiciona nova tarefa.

atualizar_status(id, novo_status): Altera o status de uma tarefa.

remover_tarefa(id): Deleta uma tarefa.

Valide se o ID existe antes de operações.

Use um set para armazenar status válidos ({"pendente", "em andamento", "concluído"}).
'''

import json

tarefas = {
    1: {"titulo": "Estudar Python", "status": "pendente"},
    2: {"titulo": "Fazer relatorio", "status": "concluido"}
}

def listar_tarefas():
    """Lista todas as tarefas."""
    return json.dumps(tarefas, indent=2)

def adicionar_tarefa():
    """Adiciona uma nova tarefa."""
    try:
        id_tarefa = int(input("Digite o ID da nova tarefa: "))
        titulo = input("Digite o título da nova tarefa: ")
        status = input("Digite o status da nova tarefa (pendente/concluido): ").lower()
        if status not in ["pendente", "concluido"]:
            return json.dumps({"status": "erro", "mensagem": "Status inválido. Use 'pendente' ou 'concluido'."}, indent=2)
        tarefas[id_tarefa] = {"titulo": titulo, "status": status}
        return json.dumps({"status": "sucesso", "id": id_tarefa}, indent=2)
    except ValueError:
        return json.dumps({"status": "erro", "mensagem": "ID inválido. Digite um número inteiro."}, indent=2)

def atualizar_status():
    """Atualiza o status de uma tarefa existente."""
    try:
        id_tarefa = int(input("Digite o ID da tarefa para atualizar o status: "))
        novo_status = input("Digite o novo status (pendente/concluido): ").lower()
        if novo_status not in ["pendente", "concluido"]:
            return json.dumps({"status": "erro", "mensagem": "Status inválido. Use 'pendente' ou 'concluido'."}, indent=2)
        if id_tarefa in tarefas:
            tarefas[id_tarefa]["status"] = novo_status
            return json.dumps({"status": "sucesso", "id": id_tarefa}, indent=2)
        else:
            return json.dumps({"status": "erro", "mensagem": "ID não encontrado"}, indent=2)
    except ValueError:
        return json.dumps({"status": "erro", "mensagem": "ID inválido. Digite um número inteiro."}, indent=2)

def remover_tarefa():
    """Remove uma tarefa existente."""
    try:
        id_tarefa = int(input("Digite o ID da tarefa para remover: "))
        if id_tarefa in tarefas:
            del tarefas[id_tarefa]
            return json.dumps({"status": "sucesso", "id": id_tarefa}, indent=2)
        else:
            return json.dumps({"status": "erro", "mensagem": "ID não encontrado"}, indent=2)
    except ValueError:
        return json.dumps({"status": "erro", "mensagem": "ID inválido. Digite um número inteiro."}, indent=2)

def exibir_menu():
    """Exibe o menu de opções."""
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Listar tarefas")
    print("2. Adicionar tarefa")
    print("3. Atualizar status da tarefa")
    print("4. Remover tarefa")
    print("5. Finalizar programa")
    print("-----------------------------")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        resultado = listar_tarefas()
        print("\n--- Lista de Tarefas ---")
        print(resultado)
    elif opcao == '2':
        resultado = adicionar_tarefa()
        print("\n--- Adicionar Tarefa ---")
        print(resultado)
    elif opcao == '3':
        resultado = atualizar_status()
        print("\n--- Atualizar Status ---")
        print(resultado)
    elif opcao == '4':
        resultado = remover_tarefa()
        print("\n--- Remover Tarefa ---")
        print(resultado)
    elif opcao == '5':
        print("\nFinalizando o programa...")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
