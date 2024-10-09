import requests
import json
import time
import datetime

while True:
    requisicao = requests.get("link")
    cotacao = json.loads(requisicao.text)
    print(time.time(),datetime.datetime.now())
    print(cotacao["valores"])
    print(cotacao["valores"]["USD"])
    print(cotacao["valores"]["USD"]["valor"])
    time.sleep(50)