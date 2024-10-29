import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.sampledata.iris import flowers as dados

print(dados.shape)
print(dados.head(3))

med_s1 = np.mean(dados['sepal_length'])
print(med_s1)

med_sw = np.mean(dados['sepal_width'])
print(med_sw)

med_p1 = np.mean(dados['petal_length'])
print(med_p1)

med_pw = np.mean(dados['petal_width'])
print(med_pw)

print(type(dados))

mediana_s1 = np.median(dados['sepal_length'])
print(mediana_s1)

mediana_sw = np.median(dados['sepal_width'])
print(mediana_sw)

mediana_p1 = np.median(dados['petal_length'])
print(mediana_p1)

mediana_pw = np.median(dados['petal_width'])
print(mediana_pw)

moda_s1 = dados["sepal_length"].mode()
print(moda_s1)

moda_sw = dados["sepal_width"].mode()
print(moda_sw)

moda_p1 = dados["petal_length"].mode()
print(moda_p1)

moda_pw = dados["petal_width"].mode()
print(moda_pw)

p10 = np.quantile(dados['sepal_length'],0.10)
print(p10)

p50 = np.quantile(dados['sepal_length'],0.50)
print(p50)

q1 = np.quantile(dados['sepal_length'],0.25)
print(q1)

q3 = np.quantile(dados['sepal_length'],0.75)
print(q3)

print(dados.describe())

x = dados["sepal_length"]
y = dados["sepal_width"]
plt.scatter(x,y)
plt.xlabel("sepal_length")
plt.ylabel("sepal_width")
plt.plot(np.mean(x),np.mean(y),"or")
plt.plot(np.median(x),np.median(y),"oy")
plt.plot(x.mode(),y.mode(),"og")
plt.show()

x2 = dados["petal_length"]
y2 = dados["petal_width"]

x = dados["sepal_length"]
y = dados["sepal_width"]
plt.scatter(x2,y2)
plt.xlabel("sepal_length")
plt.ylabel("sepal_width")
plt.plot(np.mean(x2),np.mean(y2),"or")
plt.plot(np.median(x2),np.median(y2),"oy")
plt.show()