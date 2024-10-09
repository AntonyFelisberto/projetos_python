#Meta caracteres . ^ $ * + ? { } [ ] \ | ( )
# \w é igual a [a-zA-Z0-9À-ú_]
# \W é igual a [^a-zA-Z0-9À-ú_], todas as letras maiusculas sempre negam tudo
# \d digitos de 0 a 9 
# \D é igual a [^0-9]
# \s é igual a espaços [ \r\n\f\n\t]
# \b contem borda no começo ou fim, \bflo
# \b não contem borda no começo ou fim, \bflo

#re.A ASC
#re.I IGNORE CASE
#re.M Multiline
#re.S Dotall
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

print(re.findall(r'[a-z]+',texto,flags=re.IGNORECASE))
print(re.findall(r'[a-zA-Z]+',texto))
print(re.findall(r'[a-zA-Z0-9]+',texto))
print(re.findall(r'[a-zA-Z0-9À-ú]+',texto))
print(re.findall(r'\w+',texto))
print(re.findall(r'\w+',texto,flags=re.A))
print(re.findall(r'\W+',texto))
print(re.findall(r'\W+',texto,flags=re.A))
print(re.findall(r'\d+',texto,flags=re.I))
print(re.findall(r'\D+',texto,flags=re.I))
print(re.findall(r'\s+',texto,flags=re.I))
print(re.findall(r'\S+',texto,flags=re.I))
print(re.findall(r'\be\w+',texto,flags=re.I))
print(re.findall(r'\w+e\b',texto,flags=re.I))
print(re.findall(r'\b\w{4}\b',texto,flags=re.I))
print(re.findall(r'\w{4}',texto,flags=re.I))
print(re.findall(r'flores\B',texto,flags=re.I))

textos = """
000.111.111-07,
000.888.111-07 DED
000.777.111-07 EAD
000.555.111-07 WASD
"""
print(re.findall(r"^\d{3}\.\d{3}\.\d{3}\-\d{2}",textos))
print(re.findall(r"^\d{3}\.\d{3}\.\d{3}\-\d{2}",textos,flags=re.M))
textos = """O joão gosta de folia E adora ser amado """
print(re.findall(r"^o.*o$",textos,flags=re.I))
textos = """O joão gosta de folia \n E adora ser amado """
print(re.findall(r"^o.*o$",textos,flags=re.I | re.S))