from datetime import date
atual = date.today().year
nasc = int(input("digite ano de nascimento"))
idade = atual - nasc
if(idade>=18):
    print("alistamento obrigatorio")
else:
    print("não obrigatorio")