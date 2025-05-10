# Atividades Práticas:

# 1. Crie uma classe Conta com:
'''
Atributo _saldo (privado).
Getter saldo que retorna o valor formatado (ex: R$1000.00).
Setter que bloqueia valores negativos.
'''
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return f"R${self._saldo:.2f}"
    
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            self._saldo = valor
            return ValueError("O saldo deve ser positivo.")



# 2. Classes Abstratas:
'''
Crie uma classe abstrata Animal com método comum a todas as classes-filhas.
Implemente, pelo menos, as classes Cachorro e Gato com 3 métodos para cada uma.
'''
class Mamiferos:
    def __init__(self, especie, nome, alimento):
        self.especie = especie
        self.nome = nome
        self.alimento = alimento

class Cachorro(Mamiferos):
    def __init__(self, especie, nome, alimento, raca_cao):
        super().__init__(especie, nome, alimento)
        self.raca_cao = raca_cao

    def __init__(self):
        self.cachorro = Cachorro(self.especie, self.nome, self.alimento, self.raca_cao)
        
    def latir(self):
        return "Au au"
    
    def comer(self):
        return f"{self.nome} se alimenta de {self.alimento}"
    
    def cadastro_cachorro(self):
        print("--Cadastro de Cachorro--")
        self.especie = input("Digite a especie do cachorro: ")
        self.nome = input("Digite o nome do cachorro: ")
        self.alimento = input("Digite o alimento do cachorro: ")
        self.raca_cao = input("Digite a raça do cachorro: ")
        self.cochorro.append(Cachorro(self.especie, self.nome, self.alimento, self.raca_cao))
        
        
class Gato(Mamiferos):
    def __init__(self, especie, nome, alimento, raca_gato):
        super().__init__(especie, nome, alimento)
        self.raca_gato = raca_gato

    def __init__(self):
        self.gato = Gato(self.especie, self.nome, self.alimento, self.raca_gato)
        
    def miar(self):
        return "Miau"
    
    def comer(self):
        return f"{self.nome} se alimenta de {self.alimento}"
    
    def cadastro_gato(self):
        print("--Cadastro de Gato--")
        self.especie = input("Digite a especie do gato: ")
        self.nome = input("Digite o nome do gato: ")
        self.alimento = input("Digite o alimento do gato: ")
        self.raca_gato = input("Digite a raça do gato: ")
        self.gato.append(Gato(self.especie, self.nome, self.alimento, self.raca_gato))

while True:
    print("\n--Menu--\n")
    print("1. Cadastrar cachorro")
    print("2. Latir")
    print("3. Cadastrar gato")
    print("4. Miar")
    print("5. Sair")
    opcao = int(input("\nDigite a opção desejada: "))
    if opcao == 1:
        Cachorro.cadastro_cachorro()
    elif opcao == 2:
        Cachorro.latir()
    elif opcao == 3:
        Gato.cadastro_gato()
    elif opcao == 4:
        Gato.miar()
    elif opcao == 5:
        break
        


# 3. Padrão de Acesso a Repositórios

# Crie uma classe UsuarioRepository com os seguintes métodos:
'''
- cadastrar(usuario): cadastra um usuário (dicionário com nome e email).
- listar_todos(): retorna uma lista com todos os usuários cadastrados.
- buscar_por_email(email): retorna o usuário correspondente ao email informado.
- remover(email): remove o usuário correspondente ao email informado. 
- atualizar(usuario): atualiza os dados do usuário correspondente ao email informado.
- listar_por_nome(nome): retorna uma lista com todos os usuários que possuem o nome informado.
- listar_por_email(email): retorna uma lista com todos os usuários que possuem o email informado.
- listar_por_nome_e_email(nome, email): retorna uma lista com todos os usuários que possuem o nome e email informados.
'''

# 4. DESAFIO: retorne às atividades 2 e 3 e implemente uma metaclasse dentro de seus respectivos contextos.