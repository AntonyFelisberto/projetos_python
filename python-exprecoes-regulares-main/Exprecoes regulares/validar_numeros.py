import re

def is_float(string):
    return bool(re.search("^[+-]?\d+(?:\.\d+)?$", string))
def is_int(string):
    return bool(re.search("^[+-]?\d+$", string))

test_str = "ASD@SAPDsmd@475"

print(is_float("1"))