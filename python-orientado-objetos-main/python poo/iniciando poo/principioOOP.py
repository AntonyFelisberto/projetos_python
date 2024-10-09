class Veiculo:
    um = 1
    string = "variavel global"
    def __init__(self,cor,rodas,marca):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca

    def metodo(self):
        print(self.cor,self.rodas,self.marca)

    def sobrecarga(self):
        print("novas")

class Herdar(Veiculo):
     
    def __init__(self, cor, rodas, marca):
          super().__init__(cor, rodas, marca)

    def sobrecarga(self):
        if self.rodas == "novas":
            print("novas")
        else:
             print("velhas")

carro = Veiculo("azul","arks","volksvagem")
herdado = Herdar("azul","arks","volksvagem")
print(carro)
print(carro.cor)
carro.metodo()