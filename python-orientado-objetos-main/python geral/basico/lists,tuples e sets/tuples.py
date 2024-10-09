myTuple=("iPhone", "Pixel", "Samsung")
print(myTuple) # Prints ('iPhone', 'Pixel', 'Samsung')

myTuple = ["iPhone","Pixel","Samsung"]
print(myTuple[0]) # prints iPhone
print(myTuple[7]) # throws IndexError: tuple index out of range
print(myTuple[-1]) # prints Samsung

myTuple = ("iPhone", "Pixel", "Samsung", "Oppo", "Vivo", "Redmi", "Nokia" )
print(myTuple[1:5]) # Prints ('Pixel', 'Samsung', 'Oppo', 'Vivo')

myTuple = ("iPhone", "Pixel", "Samsung")
myList = list(myTuple)
myList[1] = "onePlus"
myTuple = tuple(myList)
print(myTuple)



myTuple = ("iPhone", "Pixel", "Samsung")
myTuple[1] = "onePlus" # throws error as TypeError: 'tuple' object does not support item assignment
print(myTuple)
