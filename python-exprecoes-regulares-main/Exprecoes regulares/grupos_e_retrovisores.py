#Meta caracteres . ^ $ * + ? { } [ ] \ | ( )
# [@#a-zA-Z0-9]+ qualquer um desses e o mais liga a outras palavras
# (abc|def) especificamente esses
# () grupos (()) retrovisores
import re
from pprint import pprint


texto = """
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <p>Frase 4</p> <p>Frase 5</p><div></div>
"""

print(re.findall(r'<([pdiv]{1,3})>.*?<\/\1>',texto)) 
print(re.findall(r'(<([pdiv]{1,3})>.*?<\/\2>)',texto)) 
print(re.findall(r'(<([pdiv]{1,3})>(.*?)<\/\2>)',texto))
print(re.findall(r'<([pdiv]{1,3})>(?:.*?)<\/\1>',texto))

cpf = "aaaa 000.000.000-90 aaaaaaa"
print(re.findall(r"[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}",cpf))
print(re.findall(r"([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}",cpf))
print(re.findall(r"(([0-9]{3}\.){2}[0-9]{3}-[0-9]{2})",cpf))
print(re.findall(r"((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})",cpf))

print(re.sub(r"(<(.+?)>).+?</.+?>", r"\1", texto))
print(re.sub(r"(<(.+?)>)(.+?)(<\/\2>)", r"\1 \3 \4", texto))
print(re.sub(r"(<(.+?)>)(.+?)(<\/\2>)", r"\1 MAIS \3 FRASES \4", texto))

for tag in re.findall(r'(<([pdiv]{1,3})>.*?<\/\2>)',texto):
    print(tag)
    um,dois = tag
    pprint(um)

print(re.findall(r'<(?P<tag>[pdiv]{1,3})>(?:.*?)<\/\1>',texto))    
print(re.findall(r'<(?P<tag>[pdiv]{1,3})>(?:.*?)<\/(?P=tag)>',texto))    