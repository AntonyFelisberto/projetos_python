import math
angula = float(input("digite o angulo: "))
seno = math.sin(math.radians(angula))
print(f"o angulo de {angula} tem o seno de {seno:.2f}")
cosseno = math.cos(math.radians(angula))
print(f"o angulo de {angula} tem o cosseno de {cosseno:.2f}")
tang = math.tan(math.radians(angula))
print(f"o angulo de {angula} tem a tangente de {tang:.2f}")