#Meta caracteres . ^ $ * + ? { } [ ] \ | ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou n
import re

texto = """
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <p>Frase 4</p> <p>Frase 5</p><div></div>
"""
print(re.findall(r'<[pdiv]{1,3}>',texto))
print(re.findall(r'<[pdiv]{1,3}>.*',texto))
print(re.findall(r'<[pdiv]{1,3}>.*<\/[dpiv]{1,3}>',texto)) #greed that will continue verifying string
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[dpiv]{1,3}>',texto)) #greed that will not continue verifying string