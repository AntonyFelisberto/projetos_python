matriz = [[0,0,0],[0,0,0],[0,0,0]]

soma_par = maior = soma_col = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"digite um valor para [{linha},{coluna}]: "))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f"[{matriz[linha][coluna]:^5}]",end="")
        if(matriz[linha][coluna] %2 == 0):
            soma_par += matriz[linha][coluna]
    print()

for linha in range(0,3):
    soma_col += matriz[linha][2]

for coluna in range(0,3):
    if matriz[1][coluna] > maior:
        maior = matriz[1][coluna]

print(f"maior valor da segunda linha é {maior}")
print(f"a soma dos valores da terceira coluna é {soma_col}")
print(f"a soma dos valores pares é {soma_par}")