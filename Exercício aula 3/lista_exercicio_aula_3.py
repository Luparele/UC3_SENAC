# Atividades - Listas e Dicionários


print("_________________________________________________________________________________\n")
print("1. Filtre produtos com preço > 1000 usando list comprehension:\n")
produtos = {
    "produto1": {"nome": "tablet", "preco": 1500, "categoria": "eletrônico"},
    "produto2": {"nome": "celular", "preco": 800, "categoria": "eletrônico"},
    "produto3": {"nome": "notebook", "preco": 1200, "categoria": "eletrônico"},
    "produto4": {"nome": "mouse", "preco": 500, "categoria": "acessório"},
    "produto5": {"nome": "ipad", "preco": 2000, "categoria": "eletrônico"},
    "produto6": {"nome": "monitor", "preco": 900, "categoria": "acessório"},
}

produtos_filtrados = {chave: valor for chave, valor in produtos.items() if valor["preco"] > 1000}
print("Produtos com preço maior que R$1000:\n")
for chave, valor in produtos_filtrados.items():
    print(f"Produto: {valor['nome']}\n  Preço: {valor['preco']}\n")


print("_________________________________________________________________________________\n")

print("2.Conte quantos produtos existem por categoria (usar dicionário)\n")

categorias = {}
for produto in produtos.values():
    categoria = produto["categoria"]
    if categoria not in categorias:
        categorias[categoria] = 0
    categorias[categoria] += 1

print("Quantidade de produtos por categoria:\n")
for chave, valor in categorias.items():
    print(f"   Categoria: {chave}\n  Quantidade: {valor}\n")

print("_________________________________________________________________________________\n")

print("3.Remova duplicatas de uma lista de pedidos usando set.\n")

pedidos = [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10]
print("Lista de pedidos com duplicatas:")
print(pedidos)
pedidos_unicos = list(set(pedidos))
print("\nLista de pedidos sem duplicatas:")
print(pedidos_unicos)
print("\n_________________________________________________________________________________\n")

print("4.Uma empresa contratou seus serviços para armazenar dados de colaboradores em memória e realizar operações como:\n\n- Adicionar novos colaboradores.\n- Remover colaboradores.\n- Buscar colaborador por ID.\n- Listar colaboradores com salário acima de X.\n_____________________________________\n|-- Implemente utilizando funções --|\n_____________________________________\n")

colaboradores = {
    1: {"nome": "João", "salario": 3000},
    2: {"nome": "Maria", "salario": 4000},
    3: {"nome": "Pedro", "salario": 5000},
    4: {"nome": "Ana", "salario": 6000},
    5: {"nome": "Lucas", "salario": 7000},
}

id = int(input("Digite o ID do colaborador a ser adicionado: "))
nome = input("Digite o nome do colaborador a ser adicionado: ")
salario = int(input("Digite o salário do colaborador a ser adicionado: "))

colaboradores.update({id: {"nome": nome, "salario": salario}})
print("\nColaborador adicionado com sucesso!\n")

print("Lista de Colaboradores cadastrados após adição:\n")
for chave, valor in colaboradores.items():
    print(f"      ID: {chave}\n    Nome: {valor['nome']}\n Salário: {valor['salario']}\n")

print("_________________________________________________________________________________\n")

salario_minimo = int(input("\nDigite o salário mínimo para filtro: "))
print("\nColaboradores com salário acima do mínimo pesquisado:\n")
for chave, valor in colaboradores.items():
    if valor["salario"] > salario_minimo:
        print(f"      ID: {chave}\n    Nome: {valor['nome']}\n Salário: {valor['salario']}\n")

print("_________________________________________________________________________________\n")

id_remover = int(input("Digite o ID do colaborador a ser removido: "))
del colaboradores[id_remover]
print("\nColaborador removido com sucesso!\n")

print("Lista de Colaboradores cadastrados após remoção:\n")
for chave, valor in colaboradores.items():
    print(f"      ID: {chave}\n    Nome: {valor['nome']}\n Salário: {valor['salario']}\n")

print("_________________________________________________________________________________\n")

buscar = int(input("Digite o ID do colaborador a ser buscado: "))
id_buscar = colaboradores.get(buscar)
if id_buscar is None:
    print("\nColaborador não encontrado!\n")
else:
    print("\nColaborador encontrado:\n")
    print(f"      ID: {buscar}\n    Nome: {id_buscar.get('nome')}\n Salário: {id_buscar.get('salario')}\n")



print("_________________________________________________________________________________\n")

