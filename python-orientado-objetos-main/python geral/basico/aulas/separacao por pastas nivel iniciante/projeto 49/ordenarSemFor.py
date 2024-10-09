lista = []
for c in range(0,5):
    n = int(input("digite um valor: "))
    if c == 0:
        lista.append(n)
    elif n > lista[len(lista)-1] or n > lista[-1]:  #os dois pegam a ultima posição do array
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista(pos):
                lista.insert(pos,n)
                break
            pos+=1
print(f"{lista=}")