name    = "Foo"       # String assignment
number = 10          # An integer assignment
cost   = 10.70       # A floating point assignment

print (type(name)) # to Print the data type of the variable name
print (type(number))  # to Print the data type of the variable number
print (type(cost))  # to Print the data type of the variable cost

print ("Hi " + name + "! You have purchased " + str(number) + " fruits and your total bill is " + str(cost) + "dollars") 
# here number and cost are integers and float values and you need to convert them to string in-order to print along with other string values.

x = 10
y = 20

if (x > y) :
  print (" x is greater than y")
elif (x < y ) :
  print ("x is less than y") 
else :
  print ("x and y are equal")

"""
Data Types
Category	Data Type
Text	str
Number	int, float, complex
Boolean	bool
Binary	bytes, bytearray, memoryview
Set	set, frozenset
Sequence	list, tuple, range
Mapping	dict
type() is used to know the data type of a variable
Data casting
Constructor function	desc
int()	constructs an integer from any form of data like string, float or integer
float()	constructs a float number from any form of data like string, float or integer
str()	constructs a string from any form of data like string, float or integer
"""