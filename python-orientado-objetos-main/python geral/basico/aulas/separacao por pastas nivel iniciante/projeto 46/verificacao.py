listas = ('lapis',1.22,
          'lista',0.55,
          'dados',100.00,
          'pc',7020.00)


for p in listas:
    print(f"\nNA PALAVRA {p.upper()}",end='')
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=' ')