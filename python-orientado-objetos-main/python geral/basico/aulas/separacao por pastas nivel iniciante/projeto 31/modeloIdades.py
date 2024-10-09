from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for pessoas in range(0,7):
    nasc = int(input("digite o ano que nasceu"))
    idade = atual - nasc
    if idade >=18:
        maiores += 1
    else:
        menores += 1
    
nome = "artorias"
print(f"maiores {maiores}")
print(f"menores {menores}")
print(f"nomes com espaços a direita {nome:20}")
print(f"nomes com centralizados {nome:^20}")
print(f"nomes complementado com - e centralizados {nome:-^20}")
print(f"nomes centralizados a direita com traços {nome:->20}")
print(f"nomes centralizados a esquerda com traços {nome:-<20}")
print("python 2 %d ".format(menores))