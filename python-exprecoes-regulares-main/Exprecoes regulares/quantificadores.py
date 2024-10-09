#Meta caracteres . ^ $ * + ? { } [ ] \ | ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou n
# {n}   {10} dez especifico
# {min,max} {10,} dez ou mais {,10} 0 a dez {5,10} de cinco a dez 
# ()+
import re

texto = """
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
"""

print(re.findall(r'jo[o]ão+','Felipe',texto,flags=re.I))
print(re.findall(r'jo+ão+','Felipe',texto,flags=re.I))
print(re.findall(r'jo+ão+',texto,flags=re.I))
print(re.findall(r'jo*ão*',texto,flags=re.I))
print(re.findall(r'jo?ão*',texto,flags=re.I))
print(re.findall(r'jo{1,}ão{1,}',texto,flags=re.I))
print(re.findall(r've{3}m{1,2}',texto,flags=re.I))

texto_dois = "joão ama ser amado"
print(re.findall(r'ama[do]','Felipe',texto,flags=re.I))
print(re.findall(r'ama[od]*','Felipe',texto,flags=re.I))
print(re.findall(r'ama[do]{2}','Felipe',texto,flags=re.I))
print(re.findall(r'ama[do]{0,2}','Felipe',texto,flags=re.I))