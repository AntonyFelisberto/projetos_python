import json

file = open("automation\\languages\\json\\data.json")
data = json.load(file)
print(data)

def define(word):
    word = word.lower()
    if word in data:
        return data[word]
    
word = input("enter word: ")
defines = define(word)

if defines:
    for item in defines:
        print(item)
else:
    print("not found")