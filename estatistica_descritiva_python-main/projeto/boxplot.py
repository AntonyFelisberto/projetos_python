import seaborn as sns
from bokeh.sampledata.iris import flowers as dados
import numpy as np
import matplotlib.pyplot as plt

sns.set(style="whitegrid",color_codes=True)
sns.boxplot(data=dados)
plt.show()

plt.boxplot(dados["sepal_length"])
plt.show()

plt.boxplot(dados["petal_length"])
plt.show()

plt.style.use("ggplot")
np.random.seed(seed=0)

x = np.random.randn(1000)
y = np.random.randn(100)
z = np.random.randn(10)

fig, ax = plt.subplots()
ax.boxplot((x,y,z),vert=False,showmeans=True,meanline=True,
           labels=("x","y","z"),patch_artist=True,
           medianprops={"linewidth":2,"color":"purple"},
           meanprops={"linewidth":2,"color":"red"})
plt.plot()
plt.show()