import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from bokeh.sampledata.iris import flowers as dados

print(dados.head(3))
print(dados.shape)
print(type(dados))
print(dados.min())
print(dados.max())
print(dados.iloc[:,0:4])
print(dados.iloc[:,0:4].max())
AMP = dados.iloc[:,0:4].max() - dados.iloc[:,0:4].min()
print(AMP)
print(np.max(dados.iloc[:,0:4]))
print(np.min(dados.iloc[:,0:4]))
AMP2 = np.max(dados.iloc[:,0:4]) - np.min(dados.iloc[:,0:4])
print(AMP2)
print(np.quantile(dados["sepal_length"],0.75))

Q3 = dados["sepal_length"].quantile(0.75)
Q1 = dados["sepal_length"].quantile(0.25)
print(Q3)
print(Q1)
dqt = Q3 - Q1
print(dqt)
