import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm
from statsmodels.tsa.ar_model import AutoReg

import yfinance as yf
import pandas_datareader.data as web
yf.pdr_override()

def avalia_estacionaridade(x,cutoff = 0.01):
    pvalue = adfuller(x)[1]
    if pvalue < cutoff:
        print("Serie é estacionaria ", x.name)
        return True
    else:
        print("Serie nao é estacionaria ", x.name)
        return False
    
T = 300

a = pd.Series(index=range(T))
a.name = "SERIE A"

a[0] = 0

rho = 0.1

for t in range(1,T):
    er = np.random.randn(1)
    a[t] = a[t-1]*rho + er

med = np.mean(a)
var = np.var(a)

print(f"media {med} var {var}")

plt.plot(a)
plt.plot([0,T],[med,med])
plt.ylabel("XT");plt.xlabel("Tempo")
plt.title(f"rho {rho}")

avalia_estacionaridade(a)

plot_acf(a)

res = AutoReg(a,lags=range(1,30)).fit()
est_order = AutoReg(a,lags=range(1,30)).select_order()

print(res.params)
print(res.resid)
print(est_order)

symbols = ["^BVSP","ABEV3.SA","ITSA4.SA","PETR4.SA","VALE3.SA"]

portifolio = web.get_data_yahoo(symbols,period="1y")["Close"]

portifolio = portifolio.rename(columns={"ABEV3.SA":"ABEV3","ITSA4.SA":"ITSA4","PETR4.SA":"PETR4","VALE3.SA":"VALE3"})

retornos = portifolio.pct_change().dropna()

retornos = retornos[~retornos.isin([np.nan, np.inf, -np.inf]).any(axis=1)]

for i in retornos.colums:
    print(f"ativo = {i}")
    avalia_estacionaridade(retornos[i])

x = retornos["ITSA4"]
res = AutoReg(x,lags=range(1,30)).fit()
est_order = AutoReg(a, lags=range(1, 30)).fit().select_order(ic='aic').model.lags
print(f"ordem do modelo AutoReg {est_order}")