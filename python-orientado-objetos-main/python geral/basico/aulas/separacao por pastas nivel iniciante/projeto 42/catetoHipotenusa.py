import math
c_zero = float(input("comprimento cateto oposto: "))
c_um = float(input("comprimento cateto adjacente: "))
hi = (c_zero ** 2 + c_um ** 2) ** (1/2)
hi_metodo = math.hypot(c_zero,c_um)
print(f"a hipotenusa vai medir {hi}")
print(f"a hipotenusa vai medir no metodo {hi_metodo}")
