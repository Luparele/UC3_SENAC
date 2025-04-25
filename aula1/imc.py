nome = input("Digite o nome do aluno: ")
idade = input("Digite a idade do aluno: ")
peso = float(input("Digite o peso do aluno em kg: "))
altura = float(input("Digite a altura do aluno em metros: "))
alunos = []

imc = peso / (altura ** 2)
print(f"O IMC de {nome} é: {imc:.2f}")

status = "dentro do peso"
if imc > 25:
  status = "Sobrepeso"

print(status)

dados_aluno = {
    "nome": nome,
    "idade": idade,
    "peso": peso,
    "altura": altura,
    "imc": round(imc, 2),
    "status": status
}

def adicionar_aluno(aluno, lista_alunos):
    lista_alunos.append(aluno)

adicionar_aluno(dados_aluno, alunos)

print("Lista de alunos:")
for aluno in alunos:
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Peso: {aluno['peso']}")
    print(f"Altura: {aluno['altura']}")
    print(f"IMC: {aluno['imc']}")
    print(f"Status: {aluno['status']}")
    print()

print(alunos)