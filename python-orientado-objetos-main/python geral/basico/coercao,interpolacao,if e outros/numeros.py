a=10
b=2.5

print(dir(int))
print(dir(float))
print(b.is_integer())   #is integer só esta disponivel para floats
print(5.0.is_integer())

int.__add__(2,3)
(-2).__abs__()
print(abs(-2))

(-3.6).__abs__()
print(abs(-3.6))

from decimal import Decimal, getcontext

print(Decimal(1)/Decimal(7))
getcontext().prec = 4           #numeros apos a virgula
print(Decimal(1)/Decimal(7))
print(Decimal.max(Decimal(1),Decimal(7)))
print(Decimal(1.1)+Decimal(7.0))
print(dir())