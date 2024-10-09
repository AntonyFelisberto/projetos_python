mydict = {
    "brand" :"iPhone",
    "model": "iPhone 11"
}
print(mydict)

mydict = {
    "brand" :"iPhone",
    "model": "iPhone 11"
}
val = mydict["brand"]
print(val) # prints iPhone

mydict = {
    "brand" :"iPhone",
    "model": "iPhone 11"
}
val = mydict.get("brand")
print(val) # prints iPhone

mydict = {
    "brand" :"iPhone",
    "model": "iPhone 11",
    "cost" : "$1000"
}

mydict["cost"] ="$999"
print(mydict) # prints {'brand': 'iPhone', 'model': 'iPhone 11', 'cost': '$999'}

mydict = {
    "brand" :"iPhone",
    "model": "iPhone 11",
    "cost" : "$1000"
  
}
for mbl in mydict:
  print(mydict)

mydict = {
    "brand" :"iPhone",
    "model": "iPhone 11",
    "cost" : "$1000"
}
mydict["color"] = "Black"
print(mydict) # prints {'brand': 'iPhone', 'model': 'iPhone 11', 'cost': '$1000', 'color': 'Black'}

mydict = {
    "brand" :"iPhone",
    "model": "iPhone 11",
    "cost" : "$1000",
    "color" : "Black"
}
mydict.pop("color")
print(mydict) # prints {'brand': 'iPhone', 'model': 'iPhone 11', 'cost': '$1000'}

mydict = {
    "brand" :"iPhone",
    "model": "iPhone 11",
    "cost" : "$1000",
    "color" : "Black"
}
del mydict["color"]
print(mydict)

mydict = {
    "brand" :"iPhone",
    "model": "iPhone 11",
    "cost" : "$1000",
    "color" : "Black" 
}
del mydict  #delete everithing
print(mydict) # throws an error that 'mydict' is not defined

mydict = {
    "brand" :"iPhone",
    "model": "iPhone 11",
    "cost" : "$1000",
    "color" : "Black"
}
mydict.clear()
print(mydict) # prints {}
