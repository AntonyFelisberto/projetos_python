listas = [1,2,3,4,5]
tupla = ('1',1,2,True) #TUPLAS SÃO IMUTAVEIS
dicts = {'chave':"valor","id":1.4871}
sets_chamados_de_conjuntos = {'iii','aaaa'} #não tem item repetidos

list_vazia = []
tupla_vazia = ()
dict_vazio = {}
ser_vazio = set()

mistura = [(1,2,3), (3,4), ({"oal":11},{"sets"})]

print(tupla)
print(tupla[0])
#tupla[1] = "aaa"  #vai dar erro porque é imutavel
tupla = (1,2,3,4) #só da pra mudar se a tupla inteira for alterada
for valor in tupla:
    print(valor)

if "1" in tupla:
    print(True)

print(dicts['chave'])
print(len(dicts))
dicts['id'] = 574
dicts['novo'] = "valor"
if 2 in dicts.keys() or 2 in dicts.values():
    print(dicts.keys(),dicts.values())


sets_chamados_de_conjuntos.add("40")
sets_chamados_de_conjuntos.add(11)
sets_chamados_de_conjuntos.remove("aaaa")
if 11 in sets_chamados_de_conjuntos:
    print(True)
