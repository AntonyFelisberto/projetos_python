teste = list()  #primeiro modo de gerar lista vazia
temps = []      #segundo modo de gerar lista vazia
teste.append(temps) #alocando memoria, se algo acontecer com a lista temps isso reflete nos valores de teste
teste.append(temps[:]) #alocando somente os valores da lista

teste.append("artorias")
teste.append(11)
galera = list()
galera.append(teste)#adiciona a alocação de memória
teste[0] = "arss"
teste[1] = 22
galera.append(teste)
galera.append(teste[:])# adiciona o valor
print(galera)

galeras = [["joão",19],["ana",33],["jonas",14]]
print(galeras)
print(galeras[0])
print(galeras[0][0])

for pessoa in galera:
    print(pessoa)
    print(pessoa[0])
    print(pessoa[1])

pessoas = list()
dado = list()
for c in range(0,3):
    dado.append(str(input("digite seu nome: ")))
    dado.append(int(input("digite sua idade: ")))
    pessoas.append(dado[:])
    dado.clear()#se voce apontar na memoria, esses dados tambem serão limpos na hora de apontar os dados

print(pessoas)
print(len(pessoas))

maior = menor = 0 # as duas variaveis iniciam com 0

for p in pessoas:
    if p[1] >= 21:
        print("maior de idade")
    else:
        print("menor de idade")