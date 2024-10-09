import pandas as pd

list1 = [1,2,3,4,5,6,7,8,9,10]
df = pd.DataFrame(list1)
print(df)

dict1 = {"country": ["USA", "Mexico", "India", "Australia","China", "Indonesia"],
       "language": ["English", "spanish", "Hindi", "English", "Chinese", "Indonesian"]}
df = pd.DataFrame(dict1)
print(df)

try:
       data = pd.read_csv('example.csv') # reads example.csv csv file
       print(data)
except:
       print("error")