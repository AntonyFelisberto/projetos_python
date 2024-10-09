import re
string_teste = "o gate é feio e meu gatos tem um gate "

pattern = re.search(r'',string_teste)#r transforma a string em string crua ou seja ele tira todos os caracteres especiais exemplo se tivesse \n ele pulava linha mas com o r o \n vira um caracter normal

print(pattern)
print(pattern.group())


pattern = re.search(r'gato',string_teste)
if pattern:
    print(pattern.group())
else:
    print("não encontrou padrao")

pattern = re.search(r'gat.',string_teste)   #o ponto equivale a qualquer caracter apos o anterior
if pattern:
    print(pattern.group())
else:
    print("não encontrou padrao")

pattern = re.search(r'gat\w',string_teste)   #\w equivale a palavras
if pattern:
    print(pattern.group())
else:
    print("não encontrou padrao")

pattern = re.search(r'a{4}',string_teste)   #4 letras a apenas
if pattern:
    print(pattern.group())
else:
    print("não encontrou padrao")

pattern = re.search(r'\w{4}',string_teste)   #4 letras apenas
if pattern:
    print(pattern.group())
else:
    print("não encontrou padrao")

pattern = re.search(r'\w{4,6}',string_teste)   #de 4 a 6 letras
if pattern:
    print(pattern.group())
else:
    print("não encontrou padrao")

pattern = re.search(r'gat\w\w',string_teste)   #pode colocar a mais para colocar o padrão de busca com mais caracteres
if pattern:
    print(pattern.group())
else:
    print("não encontrou padrao")

pattern = re.findall(r'gat\w\w',string_teste)
if pattern:
    print(pattern)
else:
    print("não encontrou padrao")


pattern = re.findall(r'gat\w+',string_teste)   #w+ significa uma ou mais vezes
if pattern:
    print(pattern)
else:
    print("não encontrou padrao")

pattern = re.findall(r'gat\w*',string_teste)   #w* significa uma ou infinitas
if pattern:
    print(pattern)
else:
    print("não encontrou padrao")

pattern = re.findall(r'gat\w*.',string_teste)   #w* significa uma ou infinitas
if pattern:
    print(pattern)
else:
    print("não encontrou padrao")

pattern = re.findall(r'gat\w*\.',string_teste)   #\. significa que voce quer o ponto
if pattern:
    print(pattern)
else:
    print("não encontrou padrao")

pattern = re.findall(r'[gat]',string_teste)   #[] pode ter g a ou t
if pattern:
    print(pattern)
else:
    print("não encontrou padrao")

pattern = re.findall(r'[gat]+',string_teste)   #+ pode ter uma ou mais letras
if pattern:
    print(pattern)
else:
    print("não encontrou padrao")

pattern = re.findall(r'[gat]+\w',string_teste)   #+ pode ter uma ou mais letras
if pattern:
    print(pattern)
else:
    print("não encontrou padrao")

import requests
req = requests.get('http://lacoxinha.com.br/contato')
#expresão de e-mail
pattern = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+',req.text)   #[\w-] qualquer caracter ou traço
if pattern:
    print(pattern)
else:
    print("não encontrou padrao")