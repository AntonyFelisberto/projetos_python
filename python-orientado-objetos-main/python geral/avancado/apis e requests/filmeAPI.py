import requests
import json

def dados_filme(filme):
    print(filme)
    print(filme["Title"])
    print(filme["Actors"])
    print(filme["Year"])
    print(filme["Director"])
    print(filme["imdbRating"])

def dados_filme_array(filme):
    print(filme['totalResults'])
    print(filme["Search"][0]["Title"])
    lista = []
    for filme_ in filme:
        print(filme_["Title"])
        print(filme_["Year"])
        string = "titulo {} ano {}".format(filme_["Title"],filme_["Year"])
        lista.append(string)
        
def pesquisar(filme):
    try:
        req = requests.get(f"http://www.omdbapi.com/?t={filme}&apikey=f7b21123")
        return json.loads(req.text)
    except:
        print("erro filme não encontrado")
        return None

def lista_filmes(filme_lista,tipo):
    try:
        #req = requests.get(f"http://www.omdbapi.com/?s={filme_lista}&type={tipo}&page={str(page)}&apikey=f7b21123")req = requests.get(f"http://www.omdbapi.com/?s={filme_lista}&type={tipo}&page={str(page)}&apikey=f7b21123")
        req = requests.get(f"http://www.omdbapi.com/?s={filme_lista}&type={tipo}&apikey=f7b21123")
        print(req.status_code)
        print(req.text)
        return json.loads(req.text)
    except:
        print("erro")
        return None


if __name__ == "__main__":
    sair = False
    try:
        dados_filme_array(lista_filmes("matrix","movie"))
    except Exception as error:
        print("erro ",error)

    while not sair:
        filme = input("filme: ")
        objeto = pesquisar(filme)
        
        if not str(objeto).__contains__("False") and objeto != None:
            dados_filme(objeto)
        else:
            print("erro encontrado")
        
        sair = True if input("deseja sair do sistem Y ou N: ").lower == "y" else False

def outra_api():
    cabecalho = {"User-agent":"Windows 12","Referer":"https://google.com","cf-ipcountry":"US"}
    meus_cookies = {"ultima-visita":"10-10-2020"}
    dados = {"username":"antony","password":"123456789"}
    requests.get(f"https://putsreq.com/jovdE3QYY00Z9j8QUegR",headers=cabecalho,cookies=meus_cookies,data=dados)
