#api twitter
#entrar no site e criar uma aplicação
#gerar token
#pip install oauth2
import json
import oauth2
import pprint
import urllib.parse as parse
from oop import Twiter
import time

consumer_key = "PEGAR NO SITE"
consumer_secret = "PEGAR NO SITE"
token_key = "PEGAR NO SITE"
token_secret = "PEGAR NO SITE"

consumer = oauth2.Consumer(consumer_key,consumer_secret)
token = oauth2.Token(token_key,token_secret)
cliente = oauth2.Client(consumer,token)

query = parse.quote(input("concatenar na consulta"),safe='') #.quote converte os caracteres como # para a linguagem do browser
requisicao = oauth2.request("link_de_consulta"+query,method="POST")

print(requisicao)
print(type(requisicao[0]),type(requisicao[1]))  #a requisição pode vir com varios tipos de valores

decodificar = requisicao[1].decode()
requisicao_objeto = json.loads(decodificar)

print(requisicao_objeto)
pprint.pprint(requisicao_objeto)
pprint.pprint(requisicao_objeto["status"])
pprint.pprint(requisicao_objeto["status"][0]["user"]) #PEGANDO OBJETO DENTRO DE OBJETO
pprint.pprint(requisicao_objeto["status"][0]["user"]["screen_name"]) #PEGANDO OBJETO DENTRO DE OBJETO DENTRO DE OBJETO
pprint.pprint(requisicao_objeto["status"][0]["text"])

for twit in requisicao_objeto["statuses"]:
    print(twit["user"]["screen_name"])
    print(twit["user"])

twiter = Twiter(consumer_key,consumer_secret,token_key,token_secret)
twiter.tweet("arrrrr")
for i in range(1,100):
    resp = twiter.tweet(str(i))
    print(resp)
    time.sleep(5)