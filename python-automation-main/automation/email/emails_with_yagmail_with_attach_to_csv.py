import yagmail
import os
import pandas

sender = "YOUR EMAIL"

yag = yagmail.SMTP(user=sender,password="YOUR PASSWORD")

df = pandas.read_csv("automation\\email\\file\\contacts.csv")

for index,row in df.iterrows():
    receiver = row["email"]
    subject = "HELLO"
    content = [f"""    HELLO MY LITLE FRIEND {row["name"]} amount to pay {row["amount"]}    ""","automation\\email\\file\\contacts.csv"]
    yag.send(to=receiver,contents=content,subject=subject)