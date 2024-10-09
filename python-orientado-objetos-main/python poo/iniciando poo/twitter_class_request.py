import oauth2
import urllib.parse as parse
import json

class Twiter:
    def __init__(self,consumer_key,consumer_secret,token_key,token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.token_key = token_key
        self.token_secret = token_secret
        self.conexao()

    def conexao(self):
        self.consumer = oauth2.Consumer(self.consumer_key,self.consumer_secret)
        self.token = oauth2.Token(self.token_key,self.token_secret)
        self.cliente = oauth2.Client(self.consumer,self.token)

    def tweet(self,new_tweet):
        query = parse.quote(new_tweet,safe='') #.quote converte os caracteres como # para a linguagem do browser
        requisicao = self.cliente.request("link_de_consulta"+query,method="POST")
        decodificar = requisicao[1].decode()
        requisicao_objeto = json.loads(decodificar)
        return requisicao_objeto