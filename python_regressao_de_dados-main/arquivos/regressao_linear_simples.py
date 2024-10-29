import numpy as np
from sklearn.linear_model import LinearRegression

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
prev = list(range(0,1))
prev[0] = int(input())

x = np.asarray(x)
x = x.reshape(-1,1)
y = np.asarray(y)

model = LinearRegression()
model.fit(x,y)

prev = np.asarray(prev)
prev = prev.reshape(-1,1)

resp = model.predict(prev.reshape(-1,1))
print(f"resultado da previsâo {resp}")