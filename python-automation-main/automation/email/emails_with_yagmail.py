import yagmail

sender = "YOUR EMAIL"
receiver = "uxhmxlkzc@laste.ml"

subject = "HELLO"

content = """
HELLO MY LITLE FRIEND
"""

yag = yagmail.SMTP(user=sender,password="YOUR PASSWORD")
yag.send(to=receiver,contents=content,subject=subject)