import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("projeto/data/PETR4.SA.csv")
print(df.head(3))
print(type(df))
print(df.shape)
print(df.tail(3))
print(df.info())
print(df.describe())

print(df["Close"].hist())
plt.xlabel("Preço",size=14)
plt.ylabel("Frequência",size=14)

plt.plot(df["Close"].median(),0,"*r")
plt.plot(df["Close"].mean(),0,"og")
plt.show()

df.iloc[:,0:6].boxplot()
plt.show()

sns.boxplot(data=df.iloc[:0,0:6])
plt.show()

df.iloc[:,0:6].plot()
plt.show()