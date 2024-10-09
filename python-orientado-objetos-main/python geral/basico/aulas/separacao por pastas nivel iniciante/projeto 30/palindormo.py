frase = str(input("digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras) #junta tudo sem espaços
inverso = ""
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]

print(junto,inverso)

if junto == inverso:
    print("é palindromo")
else:
    print("não é palindromo")

inverso = junto[::-1]   #fazendo o fatiamento do inicio ao fim de tras para frente