from cliente import Cliente
from conta import Conta

cliente = Cliente("artorias","400.289.227-07",10)
print(cliente.nome)
print(cliente)      #utiliza o metodo __str__ pra fazer o print

conta = Conta(cliente,145.47)
print(conta)    #metodo str sem sobracarga de str
print(conta.cliente.idade,conta.cliente.cpf,conta.cliente.nome)

conta.retorna_saldo()
conta.sacar(float(input("digite quanto quer sacar: ")))
