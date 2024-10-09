import yagmail
import pandas
import os

sender = "YOUR EMAIL"
receiver = "uxhmxlkzc@laste.ml"

subject = "HELLO"

yag = yagmail.SMTP(user=sender,password="YOUR PASSWORD")
df = pandas.read_csv("automation\\email\\contacts.csv")
print(df)

for index,row in df.iterrows():
    content = f"""My email to {row["name"]}"""
    yag.send(to=row['email'],contents=content,subject=subject)