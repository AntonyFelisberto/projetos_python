mylist=["iPhone","Pixel","Samsung"]
print(mylist) # prints ['iPhone', 'Pixel', 'Samsung']

mylist=["iPhone","Pixel","Samsung"]
print(mylist[0]) # prints iPhone
print(mylist[7]) # throws IndexError : list index out of range
print(mylist[-1]) # prints Samsung

mylist = ["iPhone", "Pixel","Samsung", "Oppo", "Vivo", "Redmi", "Nokia" ]
print(mylist[1:5]) # Prints ['Pixel', 'Samsung', 'Oppo', 'Vivo']

mylist = ["iPhone", "Pixel", "Samsung", "Nokia" ]
mylist[1] = "OnePlus"
print(mylist) # prints ['iPhone', 'OnePlus', 'Samsung', 'Nokia']