import re
from pprint import pprint

regex = re.compile(    
    r'^'
    r'(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*[0-9])'
    r'(?=.*[ -\/:-@[-`{-~])'
    r'.{12,}'
    r'$',
    flags=re.M)

test_str = "ASD@SAPDsmd@475"

print(regex.findall(test_str))