esta_chovendo = True
asd = "Hoje estou "+("seco","molhado")[esta_chovendo] #(opcao_falsa,opcao_verdadeira)[escolha_entre_as_duas]
print(asd)

esta_como = False
asd = "Hoje estou "+("molhado" if esta_como else "seco")
print(asd)

if '2' not in asd:
    print(True)

x = 3
y = x
z = 3
print(x is y,y is z,x is not z)

lista_a = [1,2,34,5]
lista_b = lista_a
lista_z = [1,2,34,5]

print(lista_a is lista_b,lista_b is lista_b,lista_b is not lista_b)