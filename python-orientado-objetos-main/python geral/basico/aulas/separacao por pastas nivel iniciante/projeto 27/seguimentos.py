r_um = float(input("primeiro seguimento"))
r_dois = float(input("segundo seguimento"))
r_tres = float(input("terceiro seguimento"))
if r_um < r_dois + r_tres and r_dois < r_um + r_tres and r_tres < r_um + r_dois:
    print("seguimentos forman um triangulo")
else:
    print("seguimentos não forman um triangulo")

print(r_um ** 2)
print('{:=^40}'.format(' EXIBINDO ')) # {:=^40} vai exibir o = em espaços antes e após a variavel do format, o ^ é quem faz isso
