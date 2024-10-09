frase = "meus primeiros testes"
print(frase.count("o"))
print(frase.upper().count("o"))
print(len(frase))
print(len(frase.strip()))
print(frase.count("O"))
print(frase.replace("testes","nadas"))
frase = frase.replace("testes","nadas")
print("teste" in frase)
print(frase.find(" "))
print(frase.find("primeiros"))
print(frase.find("PRIMEIROS"))
print(frase.lower().find("PRIMEIROS"))  #caso retorne -1 é que não encontrou
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3]) #pega a posição especifica [2] e mostra a letra [3]
print(frase[5])
print(frase[5:10])
print(frase[:10])
print(frase[1:10:2])
print(frase[1::2])
print(frase[::2])
print("""UM THASKJDNASDNKASNDNASKNDASNDKNASDASDNASD
ASDJALSDJLKASJDLAJSDLJASLDJLASJDLJASLDJASJDLJASLDJ
OIWUQEOIQUWOEUQOWIUEOIUQWEUQWSADMAIOSJDOAJSDASDJ
SJDASJDOASJDLASJ,XNCISAERUQWRQAJRIOJQWR""")

nome = "artorias sama de conovertico"
print(len(nome) - nome.count(" "))
print(nome[:8] == "artorias")
print(nome[:8].lower().strip() == "artorias")
print(nome[:8].strip() == "artorias")
print(f"a letra o apareceu na posição {nome.find('o')+1}")
print(f"a ultima letra o apareceu na posição {nome.rfind('o')+1}")
nome = nome.split()
print(nome[len(nome)-1])