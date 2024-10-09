from datetime import datetime

pessoas = {"nome":"artorias","sexo":"M","idade":22}
print(pessoas)
print(pessoas["nome"],pessoas["idade"])
print(f"o {pessoas['nome']} tem {pessoas['idade']} anos")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.values():
    print(k)

for k in pessoas.keys():
    print(k)

for k,v in pessoas.items():
    print(f"chave {k} valor {v}")

pessoas['nome'] = 'arkham'

pessoas['peso'] = 77.4

del pessoas["sexo"]

brasil = []
estado = {"uf":"rio de janeiro","sigla":"RJ"}
estado_dois = {"uf":"são paulo","sigla":"SP"}
brasil.append(estado,estado_dois)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['uf'])

estados = dict()
brasil = list()
for c in range(0,3):
    estados['uf'] = str(input("unidade federativa: "))
    estados['sigla'] = str(input("sigla do estado: "))
    estados['média'] = float(input(f"digite a nota para o {estados['uf']}"))
    estados['aposentar'] = int(input("digite sua idade: ")) + ((int(input("digite seu ano de contratação: "))+35)-datetime.now().year)

    #brasil.append(estados)#alocamento de memória
    #brasil.append(estados[:])#em dicts não é possivel fatiar para passar os valores, é necessario usar o copy

    brasil.append(estados.copy())#maneira de passar os valores para o dict
    estados.clear()

print(brasil)
for e in brasil:
    print(e)
    for k,v in e.items():
        print(f"o campo {k} tem valor {v}")

