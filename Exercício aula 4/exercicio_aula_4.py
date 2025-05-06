'''
Crie um programa que:

- Armazene usuários (nome, e-mail) em um arquivo.
- Liste todos os usuários.
- Permita excluir um usuário.
'''

import os

def armazenar_usuario(nome_arquivo="usuarios.txt"):
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(f"{nome},{email}\n")
    print(f"\nUsuário '{nome}' armazenado com sucesso!")
    print("\n---------------//------------------")

def listar_usuarios(nome_arquivo="usuarios.txt"):
    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                print("Não há usuários cadastrados.")
                print("\n---------------//------------------")
                return
            print("\nLista de Usuários:\n")
            for i, linha in enumerate(linhas):
                nome, email = linha.strip().split(",")
                print(f"{i+1}.   Nome: {nome}\n   E-mail: {email}")
                print("\n---------------//------------------\n")
    except FileNotFoundError:
        print("Ainda não há usuários cadastrados.")

def excluir_usuario(nome_arquivo="usuarios.txt"):
    listar_usuarios(nome_arquivo)
    try:
        indice_excluir = int(input("Digite o número do usuário que deseja excluir: ")) - 1
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        if 0 <= indice_excluir < len(linhas):
            usuario_excluido = linhas.pop(indice_excluir).strip().split(",")
            with open(nome_arquivo, "w") as arquivo:
                arquivo.writelines(linhas)
            print(f"Usuário '{usuario_excluido[0]}' excluído com sucesso!")
            print("\n---------------//------------------")
        else:
            print("Número de usuário inválido.")
    except ValueError:
        print("Por favor, digite um número.")
    except FileNotFoundError:
        print("Ainda não há usuários cadastrados para excluir.")
        print("\n---------------//------------------")

def creditos():
    print("\n       --- Créditos ---\n")
    print("Desenvolvido por Eduardo Luparele")
    print("   Data: 06 de Maio de 2025")
    print("\n---------------//------------------")

def menu():
    while True:
        print("\n   --- Menu ---\n")
        print("1. Adicionar Usuário")
        print("2. Listar Usuários")
        print("3. Excluir Usuário")
        print("4. Créditos")
        print("5. Sair\n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            armazenar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            excluir_usuario()
        elif opcao == "4":
            creditos()
        elif opcao == "5":
            print("\nSaindo do programa. Até mais!\n")
            print("          -------")
            print("           ----- ")
            print("            ---  ")
            print("             -   \n")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()