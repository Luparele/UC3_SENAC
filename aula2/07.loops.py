# Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja", "uva"]
for fruta in frutas:
    print(fruta.upper())

# Com enumerate para índice e valor
for indice, fruta in enumerate(frutas, start=1):
    print(f"{indice}. {fruta}")

# Range
for i in range(5):  # 0 a 4
    print(i)

for i in range(1, 11, 2):  # 1, 3, 5, 7, 9 o primeiro parametro é o inicio, o segundo é o fim e o terceiro é o passo de 2 em 2
    print(i)

# "List comprehension"
quadrados = [x**2 for x in range(10)] # Para cada x da lista os x de 0 a 9 ele eleva ao quadrado
print(quadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]