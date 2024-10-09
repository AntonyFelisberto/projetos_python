ficha = list()

while True:
    nome = str(input("NOME: "))
    nota_um = float(input("NOTA 1: "))
    nota_dois = float(input("NOTA 2: "))
    media = (nota_um+nota_dois)/2
    ficha.append([nome,[nota_um,nota_dois],media])
    resp = str(input("Deseja continuar S ou N: "))
    if resp in "Nn":
        break

print(ficha)
print(f"{'No.':<4}{'NOME.':<10}{'MÉDIA.':>8}")
for i,a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")

while True:
    print("-"*35)
    opc = int(input("Mostra notas de qual aluno? (999 interrompe):"))
    if opc == 999:
        print("FINALIZADO")
        break
    if opc <= len(ficha) -1:
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}") #esta com 2 posições pois é uma lista composta