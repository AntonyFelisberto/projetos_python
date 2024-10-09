import sys
from locale import setlocale,LC_ALL
from collections.abc import MutableSequence
import abc

setlocale(LC_ALL, "pt_BR") #setando locale

####################################################################################################################################################################
class Televisao():
    def __init__(self,marca,ano,n_canais,preco,propriedade):
        self.marca = marca
        self.ano = ano
        self.n_canais = n_canais
        self.preco = preco
        self.__propriedade = propriedade
        self.__variedade = None
        self.__ligada = False # O __ MOSTRAS A VARIAVEL COMO PRIVADA, O PYTHON SEMPRE DEIXARA VOCE ACESSAR E ALTERAR A VARIAVEL, MAS ISSO É UMA MA PRATICA
        self._notacao = None #QUANDO TEM UM _ SIGNIFICA QUE É PROTEGIDO

    @property
    def propriedade(self):
        return self.__propriedade

    @propriedade.setter                 #usando o propriedade e disendo o tipo que ele sera
    def propriedade(self,propriedade):
        self.__propriedade = propriedade

    def diminuir_canais(self):
        self.n_canais -= 1

    def aumente_canais(self,valor):
        self.n_canais += valor

    def ligar_tv(self):
        self.__ligada = True
        print("TV LIGADA")

    def desligar_tv(self):
        self.__ligada = False
        print("TV DESLIGADA")

    def __modelo_privado(self): #O __ É PARA DIZER QUE É PRIVADO, SO PODERA SER ACESSADO DE DENTRO DA CLASSE
        print("modelo privado")

    def acessar_modelo(self):
        self.__modelo_privado()
        return f"acessando modelo privado {self.__ligada}"
    
    def set_marca(self,marca):
        self.marca = marca

    def get_marca(self):
        return self.marca

    def set_ligada(self,valor):
        self.__ligada = valor

    def get_ligada(self):
        return self.__ligada
    
    def set_variedade(self,variedade):
        self.__variedade = variedade
    
    def get_variedade(self):
        return self.__variedade

    def notacao(self):
        return self._notacao

    variedade = property(fget= get_variedade,fset= set_variedade)


tv = Televisao("kk",2015,20,1905.89,"novas")
print(tv)
print(type(tv))

tv.acessar_modelo()
tv.propriedade = "novamente"
print(tv.propriedade)

tv.variedade = "supra"
print(tv.variedade)

lg =tv 
print(lg) #mesmo endereco de memoria, entao se alterar um o outro sera alterado tbm

lg = None #eliminar referencia de memoria

#tv.__modelo_privado()  #dara erro pois o metodo é privado

print(sys.argv)
#sys.exit(0)
####################################################################################################################################################################
class Pessoa:
    num_pessoas = 0
    _num_pessoa = 0
    def __init__(self,idade):
        self.__idade = idade
        Pessoa.num_pessoas += 1
        Pessoa._num_pessoa += 1

             
    def get_num_pessoas(self): 
        return Pessoa._num_pessoa
    
    def get_num_pessoas_sem_instancia(): 
        return Pessoa._num_pessoa
    
    @staticmethod
    def get_num_pessoas_funcionando_em_instancia_e_classe(): #quando se usa staticmethod nao precisa de self
        return Pessoa._num_pessoa
    
p1 = Pessoa(12)
p2 = Pessoa(18)
p3 = Pessoa(13)
print(p3._num_pessoa)

#Pessoa.get_num_pessoas() #vai dar erro pois como tem o self voce precisa passar um objeto como o p1,p2 ou p3
print(p3.get_num_pessoas())

Pessoa.get_num_pessoas_sem_instancia()
#print(p3.get_num_pessoas_sem_instancia()) #vai dar erro pois como nao tem o self a propria instancia ja é entendida como argumento

Pessoa.get_num_pessoas_funcionando_em_instancia_e_classe()
print(p3.get_num_pessoas_funcionando_em_instancia_e_classe())
####################################################################################################################################################################
class Funcionario():    #por padrao toda classe herda do tipo object, que contem metodos especificos de classes
    def __init__(self,nome,cpf,salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def mostrar_bonus(self):
        return self.salario * 0.10

class Gerente(Funcionario):
    def __init__(self,nome,cpf,salario,senha,qtd_funcionarios):
        super().__init__(nome,cpf,salario)              #usando o super voce inicializa a herança sem passar o self
        #Funcionario.__init__(self,nome,cpf,salario)    #usando a propria classe para herança voce precisar passar o self
        self.senha = senha
        self.qtd_funcionarios = qtd_funcionarios

    def validacao(self,senha):
        if self.senha == senha:
            print("Acesso valido")
            return True
        else:
            print("Acesso invalido")
            return False
        
    def mostrar_bonus(self):#metodo override
        return self.salario * 0.10 + self.qtd_funcionarios * 0.10
        
class Secretaria(Funcionario):
    def __init__(self,nome,cpf,salario,senha,qtd_gerentes):
        super().__init__(nome,cpf,salario)              #usando o super voce inicializa a herança sem passar o self
        self.senha = senha
        self.qtd_gerentes = qtd_gerentes
    
    def mostrar_bonus(self):    #metodo override
        return self.salario * 0.10 + self.qtd_gerentes * 0.10
    
class GestaoDeBonus:
    def __init__(self,total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self,funcionario):
        if hasattr(funcionario,"mostrar_bonus"):
            self._total_bonificacoes += funcionario.mostrar_bonus()
        else:
            print(f"metodo nao implementado para a classe {self.__class__.__name__} para o objeto de parametro")

    def registra_isinstance(self,funcionario):
        if isinstance(funcionario,Funcionario):
            self._total_bonificacoes += funcionario.mostrar_bonus()
        else:
            print(f"metodo nao implementado para a classe {self.__class__.__name__} para o objeto de parametro")

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes
    

class Engenheiro:
    def __init__(self,nome):
        self.nome = nome

e = Engenheiro("art")
g = Gerente("kratos",987,5000,1234,10)
s = Secretaria("ask",345,4000,759,5)
s2 = Secretaria("nm",645,4000,789,5)
gestao = GestaoDeBonus()
gestao.registra(g)
gestao.registra(s)
gestao.registra(e)
print(gestao.total_bonificacoes)
####################################################################################################################################################################
class ClubeGerentes:
    def __init__(self,nome,funcionarios):
        self.nome = nome
        self._funcionarios = funcionarios

    def listagem(self):
        return self._funcionarios
    
    def tamanho(self):
        return len(self._funcionarios)

class ClubeGerentesSeComportandoComDuckType:
    def __init__(self,nome,funcionarios):
        self.nome = nome
        self._funcionarios = funcionarios

    def listagem(self):
        return self._funcionarios
    
    def tamanho(self):
        return len(self._funcionarios)
    
    def __getitem__(self,item):         #implementando o getitem para se comportar como uma lista
        return self._funcionarios[item] # esses tipos de comportamento sao chamados dunder methods, para pesquisar use python dunder methods

    def __len__(self):
        return len(self._funcionarios)

    def add_item(self,item):
        self._funcionarios.append(item)

g = Gerente("ant",875,999,1000,2000)
g1 = Gerente("ante",85,799,100,2)
g2 = Gerente("antw",87,899,10,20)
g3 = Gerente("ants",75,99,1,200)
lista_gententes = [g,g1,g2,g3]
clube = ClubeGerentes("NiceClube",lista_gententes)

for gerente in clube.listagem():
    print(gerente.nome)

#for gerente in clube: #vai dar erro pois nao se comporta igual uma lista
#    print(gerente)
    
#print(len(clube)) #vai dar erro pois nao se comporta igual a um objeto lista

clube = ClubeGerentesSeComportandoComDuckType("NiceClube2",lista_gententes)
for gerente in clube.listagem():
    print(gerente.nome)

clube.add_item(Gerente("dsd",5,9,1,20))

print(len(clube))
####################################################################################################################################################################
class Pessoa:
    _num_pessoas = 0        

    def __init__(self,idade):
        self.__idade = idade
        Pessoa._num_pessoas += 1

    @classmethod
    def get_num_pessoas(cls):
        return cls._num_pessoas

class PessoaSlots:
    _num_pessoas = 0

    __slots__ = ["__idade","nome"] #esse atributo como nao é de instancia da classe nao entra nos slots

    def __init__(self,idade,nome):
        self.__idade = idade
        self.nome = nome
        Pessoa._num_pessoas += 1

    @classmethod
    def get_num_pessoas(cls):
        return cls._num_pessoas

p = Pessoa(6)
print(dir(p))
p.sexo = "M"        # pode ser criado um objeto na classe por fora dela, o slots serve pra encapsular e impedir isso, alem disso ele economiza memoria

pessoa = object.__new__(PessoaSlots) #usando metodos magicos
pessoa.__init__(23,"artorias") 

ps = PessoaSlots(6,"artorias")
print(dir(ps))
print(vars(ps))
#ps.altura = 1.77   #vai dar erro pois nao existe esse atributo
####################################################################################################################################################################
class A:
    def m1(self):
        print("metodo A")

class B(A):
    def m2(self):
        print("metodo B")

class C(A):
    def m2(self):           #as vezes mesmas classes podem ter o mesmo metodo, nesse caso é dado prioridade a um metodo chamado de MRO
        print("metodo C")

    def m3(self):
        print("metodo")

class D(B,C):
    pass

d = D()
print(D.mro()) #vendo o MRO
print(d.m1())
print(d.m2())
####################################################################################################################################################################

class ClubeSecretarias(MutableSequence):
    def __delitem__(self,item):
        print("delete")

    def __getitem__(self,item):
        print("coleta")

    def __len__(self,item):
        print("len")

    def __setitem__(self,item):
        print("set")

    def insert(self,item):
        print("insert")

class ClubeSecretariasVazio(MutableSequence):
    pass

class Funcionario(abc.ABC):
    @abc.abstractclassmethod
    def nome(self):
        print("nome")

    @abc.abstractclassmethod
    def senha(self):
        print("senha")

class Atendente(Funcionario):
    def nome(self):
        print("nome")

    def senha(self):
        print("senha")

class AtendenteVazio(Funcionario):
    pass



cs = ClubeSecretarias()
atendente = Atendente()
av = AtendenteVazio()  #vai dar erro pois como implementou a classe abstrata é necessario a implementação dos metodos
func = Funcionario()  #vai dar erro pois classe é abstrata ou seja nao pode ser instanciada
csv = ClubeSecretariasVazio() #vai dar erro pois classe é abstrata, vai pedir para implementar alguns metodos nela caso nao tenham os mesmos

####################################################################################################################################################################

class Pessoa:
    _num_pessoas = 0

    def __init__(self,idade):
        self.__idade = idade
        Pessoa._num_pessoas += 1

    @staticmethod           #nao entra na herança
    def get_num_pessoas(): #nao se usa nada
        return Pessoa._num_pessoas
    
p1 = Pessoa(12)
p2 = Pessoa(18)
p3 = Pessoa(13)

class Pessoa:
    _num_pessoas = 0

    def __init__(self,idade):
        self.__idade = idade
        Pessoa._num_pessoas += 1

    @classmethod
    def get_num_pessoas(cls): #inves do self se usa o cls, pois se refere a classe, entra na herança
        return cls._num_pessoas
    
p1 = Pessoa(12)
p2 = Pessoa(18)
p3 = Pessoa(13)

####################################################################################################################################################################

class Funcionario():    #por padrao toda classe herda do tipo object, que contem metodos especificos de classes
    def __init__(self,nome,cpf,salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def mostrar_bonus(self):
        return self.salario * 0.10

class Gerente(Funcionario):
    def __init__(self,nome,cpf,salario,senha,qtd_funcionarios):
        super().__init__(nome,cpf,salario)              #usando o super voce inicializa a herança sem passar o self
        #Funcionario.__init__(self,nome,cpf,salario)    #usando a propria classe para herança voce precisar passar o self
        self.senha = senha
        self.qtd_funcionarios = qtd_funcionarios

    def validacao(self,senha):
        if self.senha == senha:
            print("Acesso valido")
            return True
        else:
            print("Acesso invalido")
            return False
        
    def mostrar_bonus(self):#metodo override
        return self.salario * 0.10 + self.qtd_funcionarios * 0.10
        
class Secretaria(Funcionario):
    def __init__(self,nome,cpf,salario,senha,qtd_gerentes):
        super().__init__(nome,cpf,salario)              #usando o super voce inicializa a herança sem passar o self
        self.senha = senha
        self.qtd_gerentes = qtd_gerentes
    
    def mostrar_bonus(self):    #metodo override
        return self.salario * 0.10 + self.qtd_gerentes * 0.10
    
####################################################################################################################################################################
