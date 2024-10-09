import re

texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''
#positive lookahead #negative lookahead
print(re.findall(r"\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+",texto))
print(re.findall(r"\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)",texto))#positive lookahead
print(re.findall(r"\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)",texto))#negative lookahead
print(re.findall(r".+",texto))
print(re.findall(r"(?=.*active).+",texto))
print(re.findall(r"(?=.*[^in]active).+",texto))

#positive lookbehind #negative lookbehind
print(re.findall(r"\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+",texto))#positive lookbehind
print(re.findall(r"\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+",texto))#negative lookbehind