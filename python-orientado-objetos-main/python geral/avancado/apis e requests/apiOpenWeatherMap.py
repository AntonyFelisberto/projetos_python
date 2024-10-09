import requests
import json

cidade = input("cidade: ")
requisicao = requests.get("link"+cidade+"&appid=SUA_CHAVE")
print(requisicao.text)
objeto = json.loads(requisicao.text)
print(objeto)
print(objeto['weather'])
print(objeto['weather'][0])
print(objeto['weather'][0]["main"])
print(float(objeto['main']["temp"])-273.15)