class Conta:

    def __init__(self,cliente,saldo):
        self.cliente = cliente
        self.saldo = saldo

    def retorna_saldo(self):
        print(self.saldo)

    def depositar(self,quantidade):
        if quantidade > 0:
            self.saldo +=quantidade
        else:
            print("sem saldo")

    def sacar(self,quantidade):
        if quantidade > 0 and self.saldo >= quantidade:
            self.saldo -=quantidade
            print(self.saldo)
        else:
            print("sem saldo")

