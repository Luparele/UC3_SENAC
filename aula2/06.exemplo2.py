def verificar_palindromo():
    texto = input("Digite uma palavra ou frase: ").lower().replace(" ", "")
    if texto == texto[::-1]: # ::-1 inverte o texto da string
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")

verificar_palindromo()