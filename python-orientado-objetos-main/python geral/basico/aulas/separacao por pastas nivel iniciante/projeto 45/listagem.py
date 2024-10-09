listas = ('lapis',1.22,
          'lista',0.55,
          'dados',100.00,
          'pc',7020.00)

print("--"*40)
print(f"{'LISTAGEM DE PREÇO':^40}")
print("--"*40)

for pos in range(0,len(listas)):
    if pos % 2 == 0 :
        print(f"{listas[pos]:.<30}",end='')
    else:
        print(f"{listas[pos]:.>7.2f}")
        
print("--"*30)