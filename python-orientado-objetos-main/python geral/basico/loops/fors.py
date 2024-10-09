for i in range(10):
    print(i)

for i in range(1,11): #subtrai 1
    print(i)


for i in range(1,100,7):
    print(i)

for i in range(20,0,-3):
    print(i)

nums = [1,2,3,4,5,6,7,8,9,10]
for n in nums:
    print(n,end=" ")

texto = "meu primeiro for"
for i in texto:
    print(i,end=" ")

for n in {1,2,3,4,5,6,7,8}:
    print(n,end="")

dicts = {
    "nome":"artorias",
    "idade":1000,
    "desc":0.5
}

for attrib in dicts:
    print(attrib,dicts[attrib])

for attrib,valor in dicts.items():
    print(attrib,valor)

for valor in dicts.values():
    print(valor,end=" ")

for attributes in dicts.keys():
    print(attributes,end=" ")

pessoas = ["gui","rebecca"]
adjs = ["arkham","asylum"]
for p in pessoas:
    for a in adjs:
        print(f"{p} e {a}")

for i in [1,2,3]:
    pass

for i in range(1,11):
    if i%2 == 0:
        continue
    print(i)

for i in range(1,11):
    if i == 5:
        break
    print(i)


    