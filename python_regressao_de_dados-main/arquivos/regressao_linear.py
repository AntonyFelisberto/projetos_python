from numpy import *

def correlacao(x, y):
    covariacao = cov(x,y,bias=True)[0][1]
    variancia_x = var(x)
    variancia_y = var(y)
    return covariacao / sqrt(variancia_x * variancia_y)

def inclinacao(x, y, correlacao):
    stdx = std(x)
    stdy = std(y)
    return correlacao * (stdx / stdy)

def interceptacao(x, y, inclinacao):
    mediax = mean(x)
    mediay = mean(y)
    return mediay - mediax * inclinacao

def previsao(interceptacao, inclinacao, valor):
    return interceptacao + (inclinacao * valor)

quantity = int(input("informe a quantidade de variaveis do modelo: "))
x = list(range(0, quantity))
y = list(range(0, quantity))

print(f"Informe as {quantity} variaveis dependentes ")
for n in range(0,quantity):
    print(f"Informe o valor {n+1}")
    y[n]=int(input())

print(f"Informe as {quantity} variaveis independentes ")
for n in range(0,quantity):
    print(f"Informe o valor {n+1}")
    x[n]=int(input())

print("informe o valor que deseja prever: ")
prev = float(input(""))
cor = correlacao(x,y)
inc = inclinacao(x,y,cor)
inter = interceptacao(x,y,cor)
result = previsao(inter,inc,prev)

print("modelo ")
print("correlação: ",cor)
print("Inclinação: ",inc)
print("interceptação: ",inter)
print("Valor para prever: ",prev)
print("Resultado da previsao: ",result)