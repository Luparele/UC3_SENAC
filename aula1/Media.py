nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

def media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print("Sua média é: ", media)
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

resultado = media(nota1, nota2, nota3, nota4)
print("Resultado: ", resultado)
