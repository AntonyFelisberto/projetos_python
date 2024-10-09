cont = ('zero','um','dois','tres')
while True:
    num = int(input("digite um numero: "))
    if 0 <= num <= 20:
        break
    print("tente novamente\n",end=' ')

print(f"voce escolheu {cont[num]}")