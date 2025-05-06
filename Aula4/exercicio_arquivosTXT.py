# Crie um programa que:
'''
Armazene usuários (nome, e-mail) em um arquivo.
Liste todos os usuários.
Permita excluir um usuário.
'''

# Criando e escrevendo em um arquivo
with open('usuarios.txt', 'w') as dados:
    dados.write("Nome: Joao\nEmail: joao@email\n")
    dados.write("Nome: Maria\nEmail: maria@email\n")
    dados.write("Nome: Pedro\nEmail: pedro@email\n")
    dados.write("Nome: Ana\nEmail: ana@email\n")

# Lendo o arquivo dados
with open('usuarios.txt' ,'r') as dados:
    conteudo = dados.read()
    print(conteudo)

# Adicionando mais dados (append)
with open('usuarios.txt', 'a') as dados:
    dados.write("Nome: Alyfer\nEmail: alyfer@email\n")

# Excluindo o arquivo (importar o módulo 'os') #Sitema Operacional
import os 
if os.path.exists('usuarios.txt'):
    os.remove('usuarios.txt')
    print("Arquivo removido!")
else:
    print("Arquivo não encontrado.")

#Listar usuários
def listarUsuarios(nome_arquivo):
    '''Retorna o número de linhas de um arquivo.'''
    with open(nome_arquivo, 'r') as arquivo:
        return len(arquivo.readlines())