print(3 * 5 + 4 ** 2)
distancia = float(input("digite a distancia: "))
print(f"voce esta começando em {distancia}")
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f"o preço da passagem sera {preco}")