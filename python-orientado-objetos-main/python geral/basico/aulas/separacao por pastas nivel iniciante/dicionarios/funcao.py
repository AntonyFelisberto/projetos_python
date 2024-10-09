def perguntar():
    return input("""o que deseja realizar\n
                I - inserir usuario\n
                P - pesquisar usuario\n
                E - excluir usuario\n
                L - ler usuario\n""")

def inserir(usuarios):
    chave=input("digite o login ").upper()
    nome=input("digite o nome ").upper()
    data=input("digite o data ").upper()
    estacao=input("digite o estacao ").upper()
    usuarios[chave]=[nome,data,estacao]
    #ou usuarios[input("digite o login ")]=[input("digite o nome ").upper(),input("digite o data ").upper(),input("digite o estacao ").upper()]
    salvar(usuarios)

def salvar(usuarios:dict):
    with open("arquivo.txt","a") as arquivo:
        for chave,valor in usuarios.items():
            arquivo.write(chave+":"+str(valor))
