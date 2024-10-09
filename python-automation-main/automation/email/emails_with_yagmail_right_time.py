import yagmail
import time
from datetime import datetime as dt

sender = "YOUR EMAIL"
receiver = "uxhmxlkzc@laste.ml"

subject = "HELLO"

content = """
HELLO MY LITLE FRIEND
"""

while True:
    now = dt.now()
    if now.hour == 13 and now.minute == 15:
        yag = yagmail.SMTP(user=sender,password="YOUR PASSWORD")
        yag.send(to=receiver,contents=content,subject=subject)
        print("email enviado")
        time.sleep(60)