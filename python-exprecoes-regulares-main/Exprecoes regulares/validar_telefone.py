import re
from pprint import pprint

regex = re.compile(r"^((\(\d{2}\)\s)?(9\s)?(\d{4}-\d{4}))$",flags=re.MULTILINE)

test_str = "(43) 9 9691-6631"

for telefone in regex.findall(test_str):
    telefone_completo, ddd, nove, numero = telefone
    print(telefone_completo)