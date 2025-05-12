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
        if valor >= 0:
            self._saldo = valor
        else:
            raise ValueError("O saldo deve ser positivo.")