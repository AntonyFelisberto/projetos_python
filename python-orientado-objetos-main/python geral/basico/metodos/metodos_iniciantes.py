number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
mul = number1 * number2
print("Multiplication of given two numbers is: ", mul)
###################################################################
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
if (number1 == number2):
	print(number1, " is equal to ", number2)
elif (number1 > number2):
	print(number1, " is larger than ", number2)
else:
	print(number1, " is lesser than ", number2)
###################################################################
bill = int(input("Enter bill amount:"))
discount = int(input("Enter discount percentage:"))
output = bill - (bill * discount / 100)
print("After discount your bill is: ", output)
###################################################################
oldSalaryPerMonth = int(input("Enter your old salary per month:"))
hike = int(input("Enter your hike percentage:"))
presentSalaryPerMonth = oldSalaryPerMonth + (oldSalaryPerMonth * hike / 100)
print("After hike your present salary per month is: ", presentSalaryPerMonth)
###################################################################
kilograms = float(input("Please enter kilograms:"))
grams = kilograms * 1000
print(grams, " Grams")
###################################################################
grams = float(input("Please enter grams:"))
kilograms = grams / 1000
print(kilograms, " Kilograms")
###################################################################
investment = float(input("Enter investment:"))
interestRate = float(input("Enter interest rate:"))
time = float(input("Enter number of years:"))
interest = investment * interestRate * time / 100
print("Interest amount is: ", interest)
###################################################################
birthYear = int(input("Please enter your date of birth:"))
age = 2018 - birthYear
print("Your age is", age)
###################################################################
centimeters = int(input("Please enter centimeters:"))
millimeters = centimeters * 10
print(millimeters, " Millimeters")
###################################################################
rectangleLength = float(input("Enter length of rectangle:"))
rectangleWidth = float(input("Enter width of rectangle:"))
areaOfRectangle = rectangleLength * rectangleWidth
print("Area of rectangle is: ", areaOfRectangle)
circumferenceOfRectangle = 2 * (rectangleLength) + 2 * (rectangleWidth)
print("Circumference of rectangle is: ", circumferenceOfRectangle)
###################################################################
rupees = float(input("Please enter rupees:"))
dollars = rupees / 64
print(dollars, " Dollars")
###################################################################
days = int(input("Please enter days:"))
milliseconds = days * 24 * 60 * 60 * 1000
print(milliseconds, " Milliseconds")
###################################################################
millimeters = float(input("Please enter millimeters:"))
centimeters = millimeters / 10
print(centimeters, " Centimeters")
###################################################################
number = int(input("Please enter a number:: "))
if (number < 0):
	print("Given number is -ve")
else:
	print("Given number is +ve")
###################################################################
number = int(input("Please enter a number:"))
result = number * number
print("Squre of ", number, " is: ", result)
###################################################################
number = float(input("Enter a number:"))
result = number * (number + 1) / 2
print(result)
###################################################################
number = int(input("Enter a number:"))
result = 1
for i in range(1, number + 1):
	result = result * i
print(number, " factorial is: ", result)
###################################################################
parallelogramBase = float(input("Please enter base of parallelogram:"))
parallelogramSide = float(input("Please enter side of parallelogram:"))
circumferenceOfParallelogram = 2 * (parallelogramBase + parallelogramSide)
print("Circumference of parallelogram is: ", circumferenceOfParallelogram)
###################################################################
number = int(input("Please enter a number:"))
if (number % 2 == 0):
	print("even")
else:
	print("odd")
###################################################################
def gcd(n1, n2):
    if(n1 == 0):
        return n2
    if(n2 == 0):
        return n1

    while(n2 != 0):
        if(n1 > n2):
            n1 = n1 - n2
        else:
            n2 = n2 - n1
    return n1

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))

res = gcd(x, y)
print("\nGCD of {0} and {1} = {2}".format(x, y, res))
###################################################################
triangleSide1 = float(input("Enter the side1 of triangle:"))
triangleSide2 = float(input("Enter the side2 of triangle:"))
triangleSide3 = float(input("Enter the side3 of triangle:"))
circumferenceOfTriangle = triangleSide1 + triangleSide2 + triangleSide3
print("Circumference of triangle is: ", circumferenceOfTriangle)
###################################################################
miles = float(input("Please enter miles:"))
kilometers = miles * 1.6
print(kilometers, " Kilometers")
###################################################################
circleRadius = float(input("Please enter the radius of circle:"))
areaOfCircle = 22/7 * (circleRadius * circleRadius)
print("Area of circle is: " , areaOfCircle)
###################################################################
inp = [1000, 100, 10000, 10] # initialize list
inp.sort() # sorting the list items in ascending order
# printing last element of the list as it the largest after sorting
print ("Largest number of the list: ", inp[-1]) 
###################################################################
inp = [1000, 100, 10000, 10]; # initialize list

def largestArrElement(arr) :
 mx = arr[0]; # initialize mx with first element of the list
 n = len(arr);
  
 for i in range(1, n): 
  if arr[i] > mx: # compare every element of the list with mx and then assign largest num to mx
    mx = arr[i] 
 return mx

maxNum = largestArrElement(inp)

print ("Largest number of the list: ", maxNum)
###################################################################
temperature = float(input("Please enter temperature in fahrenheit:"))
celsius = (temperature - 32) * 5 / 9
print("Temperature in celsius: " , celsius)
###################################################################
terms = int(input("Enter how many terms: "))

first, second = 0, 1
i = 0

if terms <= 0:
   print("Invalid input")
   
elif terms == 1:
   print("\nFibonacci series up to",terms,"terms:")
   print(first)
else:
   print("\nFibonacci series up to",terms,"terms:")
   while i < terms:
     print(first)
     next = first + second
     first = second
     second = next
     i +=1
###################################################################
hours = int(input("Please enter hours:"))
minutes = hours * 60
print(minutes, " Minutes")
###################################################################
number = int(input("Enter the number: "))
for i in range(1, 11):
	print(number, " * ", i, " = ", number * i)
###################################################################
number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
sum= number1 + number2
print("Sum of the given two numbers is: ", sum)
###################################################################
char = input("Enter a character:")
if (char == 'a' or char == 'A' or char == 'e' or char == 'E' or char == 'i'
        or char == 'I' or char == 'o' or char == 'O' or char == 'u'
        or char == 'U'):
	print('Its a vowel')
else:
	print('Its a consonant')
###################################################################
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
if (number1 == number2) and (number1 == number3):
	print("All numbers are equal")
elif (number1 > number2) and (number1 > number3):
	print(number1, " is larger than ", number2, " and ", number3)
elif (number2 > number1) and (number2 > number3):
	print(number2, " is larger than ", number1, " and ", number3)
elif (number3 > number1) and (number3 > number2):
	print
	(number3, " is larger than ", number2, " and ", number1)
###################################################################
circleRadius = float(input("Please enter the radius of circle:"))
circumferenceOfCircle = 2 * 22 / 7 * circleRadius
print("Circumference of circle is: ", circumferenceOfCircle)
###################################################################
trapezoidBase1 = float(input("Please enter base1 of trapezoid:"))
trapezoidBase2 = float(input("Please enter base2 of trapezoid:"))
trapezoidSide1 = float(input("Please enter side1 of trapezoid:"))
trapezoidSide2 = float(input("Please enter side2 of trapezoid:"))
circumferenceOfTrapezoid = trapezoidBase1 + trapezoidBase2 + trapezoidSide1 + trapezoidSide2
print("Circumference of trapezoid is: " , circumferenceOfTrapezoid)
###################################################################