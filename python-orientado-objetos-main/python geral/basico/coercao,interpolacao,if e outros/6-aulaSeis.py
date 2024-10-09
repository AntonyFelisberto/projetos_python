#CONVERSÃO, COERÇÃO, TYPECASTING,CORECION EM PYTHON (CONVERTER UM TIPO EM OUTRO)
#TIPOS PRIMITIVOS E IMUTAVEIS PARA CONVERSÃO bool,int,float e str
#print("a" + 1) NÃO É POSSIVEL CONCATENAR INT E STR SOMENTE MESMOS TIPOS
print(1+int('1'))
print('1',type('1'),int('1'),type(int('1')))
print(1.3,type(1.3),int(1.3),type(int(1.3)))
print(bool(1))
print(bool(0))
print(bool(1.55))
print(bool(0.0))