class livro():

    def __init__(self):
        self.titulo = "title"
        self.tx = 4577

    def imprime(self):
        print("criado")

livros = livro()
livros.imprime()

class ads:
    def __init__(self,titulo,isbn):
        self.titulo = titulo
        self.tx = isbn

    def imprime(self,titulo,isbn):
        print("criado",titulo,isbn)

    def func(self,titulo,isbn):
        print(titulo,isbn)

adss = ads("asd","aws")
adss.imprime("no","vo")
print(hasattr(adss,"titulo"))
print(hasattr(adss,"isbn"))
setattr(adss,"titulo","novo titulo")
print(getattr(adss,"titulo"))
delattr(adss,"titulo")


class AlgoritimoBasico():
    def __init__(self,tipo_algo=None):
        self.tipo_algo = tipo_algo

algo = AlgoritimoBasico()
print(algo.tipo_algo)

class Carro(object):
    pass

class Circulo():

    #valor constante
    pi = 3.14

    def __init__(self,raio=5):
        self.raio = 5

    def area(self): #sempre se usa o self em metodos dentreo de classes, mesmo se não usalo pois ele recebe o objeto da classe
        return (self.raio * self.raio) * Circulo.pi
    
    def set_raio(self,novo_raio):
        self.raio = novo_raio

    def get_raio(self):
        return self.raio
    
circulo = Circulo()    
circulo.get_raio()
circulo.set_raio(4)

#heranças em python
class Animal:

    def __init__(self):
        print("Animal criado")

    def imprimir(self):
        print("este animal")

    def comer(self):
        print("hora de comer")

    def emitir_som(self):
        pass   #deixando o pass significa que vai preencher futuramente o código 

class Cachorro(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("cachorro criado")

    def emitir_som(self):
        print("au")

class Gato(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("cachorro criado")

    def emitir_som(self):
        print("miau")

rex = Cachorro()
rex.comer()
rex.emitir_som()
rex.imprimir()

#polimorfismos
class Veiculo():

    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        pass

    def frear(self):
        pass    #usando pass para o polimorfismo

#subclasses para polimorfismo não se usa o construtor
class Carros(Veiculo):

    def acelerar(self):
        print("carro acelerando")

    def frear(self):
        print("carro freando")

#subclasses para polimorfismo não se usa o construtor
class Motos(Veiculo):

    def acelerar(self):
        print("moto acelerando")

    def frear(self):
        print("moto freando")

listas = [Carros("porche","007"),Motos("honda","aesddd")]
print("------")
for item in listas:
    item.acelerar()
    item.frear()

    if isinstance(item,Motos):
        item.acelerar()

    print("------")