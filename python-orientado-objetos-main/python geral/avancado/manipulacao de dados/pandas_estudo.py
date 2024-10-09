import pandas as pd
from pandas import DataFrame

dados = {
    "estado":["santa catarina","rio de janeiro","tocantins","bahia","minas gerais"],
    "ano":[2004,2005,2006,2007,2008],
    "taxa_desemprego":[1.5,1.6,1.7,2.4,2.7]
}

df = DataFrame(dados)
df.head()
type(df)

DataFrame(dados,columns=['estado','ano','taxa_desemprego'])

df2 = DataFrame(dados,columns=['estado','ano','taxa_desemprego'], index=["estado","estado_um","estado_dois","estado_tres","estado_quatro"])

print(df2)
print(df2.columns)
print(df2["estado"])

df2 = DataFrame(dados,columns=['estado','ano',"taxa_crescimento",'taxa_desemprego'], index=["estado","estado_um","estado_dois","estado_tres","estado_quatro"])
print(df2)
print(df2.dtypes)
print(df2.values)
print(df2.columns)
print(df2["estado"])
print(df2(["taxa _desemprego","ano"]))
print(df2.index)
print(df2.filter(items=["estado"],axis=0))