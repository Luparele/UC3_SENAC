class Animal:
    def comer(self):
        return f"{self.nome} se alimenta de {self.alimento}"

    def __init__(self, especie, nome, alimento):
        self.especie = especie
        self.nome = nome
        self.alimento = alimento

class Cachorro(Animal):
    def __init__(self, nome, alimento, raca):
        super().__init__("Canis familiaris", nome, alimento)
        self.raca = raca

    def __str__(self):
        return f"{self.nome} é um {self.raca} e se alimenta de {self.alimento}."

    def latir(self):
        return "Au au!"

    def brincar(self):
        return f"{self.nome} está abanando o rabo e correndo!"

class Gato(Animal):
    def __init__(self, nome, alimento, raca):
        super().__init__("Felis catus", nome, alimento)
        self.raca = raca

    def __str__(self):
        return f"{self.nome} é um {self.raca} e se alimenta de {self.alimento}."

    def miar(self):
        return "Miau!"

    def ronronar(self):
        return f"{self.nome} está ronronando suavemente."

# Criando um objeto Cachorro
cachorro = Cachorro("Rex", "ração", "Pastor Alemão")

# Criando um objeto Gato
gato = Gato("Mimi", "ração", "Persa")

print("--Testes do Cachorro--")
print(Cachorro.__str__(cachorro))
print(f"Nome do cachorro: {cachorro.nome}")
print(f"Raça do cachorro: {cachorro.raca}")
print(f"O que o cachorro come: {cachorro.comer()}")
print(f"Teste do método brincar: {cachorro.brincar()}")
print(f"Teste do método latir diretamente: {cachorro.latir()}")

print("\n--Testes do Gato--")
print(f"Nome do gato: {gato.nome}")
print(f"Raça do gato: {gato.raca}")
print(f"O que o gato come: {gato.comer()}")
print(f"Teste do método ronronar: {gato.ronronar()}")
print(f"Teste do método miar diretamente: {gato.miar()}")