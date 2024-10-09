import yagmail
import os
import pandas

sender = "YOUR EMAIL"

yag = yagmail.SMTP(user=sender,password="YOUR PASSWORD")

df = pandas.read_csv("automation\\email\\file\\contacts__.csv")

def generate_file(filename,content):
    with open(filename,"w") as f:
        f.write(str(content))

for index,row in df.iterrows():
    filename = f"{row['name']}.txt"
    name = row["name"]
    receiver = row["email"]
    amount = row["amount"]
    generate_file(filename,amount)
    subject = "HELLO"
    content = [f"""    HELLO MY LITLE FRIEND {name} amount to pay {amount}    """,filename]
    yag.send(to=receiver,contents=content,subject=subject)