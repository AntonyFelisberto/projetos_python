import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("projeto/data/train.csv")
print(df.info())
print(df.describe())
print(df.head(3))
print(df.isnull().sum())
print(df.fillna(df["Age"].dropna().median(),inplace=True))
print(df.isnull().sum())
print(df.shape)
df.plot(kind="scatter",x = "Fare", y = "Survived", color = "r",linewidth = 1)
plt.show()

sns.barplot(x="Pclass",y="Survived",data=df)
plt.show()

sns.barplot(x="Sex",y="Survived",data=df)
plt.show()

survived = "survived"
not_survived = "not survived"

fig, axes = plt.subplots(nrows=1,ncols=2,figsize=(10,4))
womem = df[df["Sex"]=="female"]
men = df[df["Sex"]=="male"]

ax = sns.displot(womem[womem["Survived"]==1].Age.dropna(),bins=18,label=survived,ax=axes[0],kde=False)
ax = sns.displot(womem[womem["Survived"]==1].Age.dropna(),bins=40,label=not_survived,ax=axes[0],kde=False)


ax.set_titles("Female")
ax = sns.displot(men[men["Survived"]==1].Age.dropna(),bins=18,label=survived,ax=axes[1],kde=False)
ax = sns.displot(men[men["Survived"]==0].Age.dropna(),bins=40,label=not_survived,ax=axes[1],kde=False)


_ = ax.set_titles("Male")
plt.show()