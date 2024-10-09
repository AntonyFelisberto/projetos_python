import json

dicts = {
    "artorias":["ADS","14/02/2023","REC"],
    "KRATOS":["AMS","14/02/2223","REC"],
    "morbius":["MORBADS","14/02/1023","REC"]
}
with open("bd1.json","w") as arquivo:
    json.dump(dicts,arquivo)    #cria um arquivo

with open("bd.json","r") as arquivo:
    dic = json.load(arquivo)
    for chave,registro in dic.items():
        print(chave+":"+str(registro))

arquivo = open("arquivo.txt","w") #w substitui todo o arquivo,a só adiciona r só le o arquivo
print(type(arquivo),end="\n")
arquivo.write("escrever no txt\n")
for i in range(0, 1000):
    arquivo.write(str(i)+"\n")
arquivo.close()

arquivo = open("arquivo.txt","r") #w substitui todo o arquivo,a só adiciona r só le o arquivo
print(arquivo.read())

for linha in arquivo:
    print(linha)

arquivo = open("arquivo.png","rb") #b para ler arquivo binario
print(arquivo.read())

with open("arquivo.txt","w") as arquivo:    #with gerencia o fluxo de arquivos pra voce
    arquivo.write("asd")
    conteudo = arquivo.read()
    print(conteudo)
    conteudo = arquivo.readline()   #só le a primeira linha
    for linha in arquivo.readline():
        print(arquivo.readline())   #só le a primeira linha

with open("arquivo.txt","a") as arquivo:    
    arquivo.write("asd")



try:
    basedados = []
    with open("arquivo.data","r") as arquivo:
        for registro in arquivo.readlines():
            basedados.append(registro.split(","))
    print(basedados)
    print(basedados[0])
    print(basedados[0][0])
    print(basedados[0][0] + basedados[0][1])
    print(float(basedados[0][0]) + float(basedados[0][1]))
except:
    print("dados não encontrados")

