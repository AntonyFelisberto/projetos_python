import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

y = [2,5,2,7,5,1]
x = ["N1", "N2", "N3", "N4", "N5", "N6"]
x2 = ["var_um", "var_dois", "var_tres", "var_quatro", "var_cinco", "var_seis"]

plt.barh(x2,y,color="g")
plt.xlabel("Var eixo X",size=24)
plt.ylabel("Categorias",size=20)
plt.title("Titulo do meu grafico")
plt.show()

plt.bar(x2,y)
plt.show()

plt.pie(y,labels=x,radius=1)
plt.show()

y = [6,8,3,1,9]
x1 = [1,2,3,4,5]
x = ["seg", "ter", "qua", "qui", "sex", "var_seis"]

plt.plot(x1,y,"o-g")
plt.xlabel("Eixo X",size=20)
plt.ylabel("Eixo Y",size=20)
plt.title("Titulo do gráfico",size=15)
plt.show()

plt.plot(x1,y,"o-c")
plt.xlabel("Eixo X",size=20)
plt.ylabel("Eixo Y",size=20)
plt.title("Titulo do gráfico",size=15)
plt.show()

x = np.random.randn(1000)
print(x)

plt.hist(x,bins=4,color="g")
plt.xlabel("Eixo X")
plt.ylabel("Frequências")
plt.show()