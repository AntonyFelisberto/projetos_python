from math import factorial
n = int(input("digite um numero para fatorial:"))
f = factorial(n)
print(f"fatorial com biblioteca {f}")
fato = n
c = 1
while fato > 0:
    print(f"{fato}",end='')
    print(' x ' if fato > 1 else ' = ',end='')
    c *= fato
    fato -= 1

print(f"fatorial sem biblioteca {c}")
