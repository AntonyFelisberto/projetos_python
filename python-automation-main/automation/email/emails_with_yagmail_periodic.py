import yagmail
import time
sender = "YOUR EMAIL"
receiver = "uxhmxlkzc@laste.ml"

subject = "HELLO"

content = """
HELLO MY LITLE FRIEND
"""

while True:
    yag = yagmail.SMTP(user=sender,password="YOUR PASSWORD")
    yag.send(to=receiver,contents=content,subject=subject)
    print("email enviado")
    time.sleep(60)