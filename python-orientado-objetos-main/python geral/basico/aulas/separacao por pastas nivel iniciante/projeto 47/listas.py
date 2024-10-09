num = [1,2,3,4,5]
num[2] = 5
num.append(8)
num.sort()
num.insert(2,0) #na posição 2 inserir 0
num.pop()
num.pop(2) #remover posição 2
num.remove(2) #remove o numero especificado somente a primeira vez que encontralo
if 4 in num:
    num.remove(4)

num.sort(reverse=True)
print(len(num))
print(num)

valores = list()
for cont in range(0,6):
    valores.append(int(cont))
    valores.append(int(input("digite um valor: ")))

print(max(valores))
print(min(valores))

cd = num
cd[2] = 10 #vai alterar as duas listas pois pega o alocamento de memoria

b = num[:]
b[2] = 8   #não vai alterar as duas pois esta pegando os valores somente

for v in num:
    print(f"{v}")

for c,v in enumerate(num):
    print(f"valor {v} chave {c}")
    