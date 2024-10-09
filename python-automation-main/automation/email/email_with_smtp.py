import smtplib
import os

sender = "YOUR EMAIL"
receiver = "WHO WILL RECEIVE THE EMAIL"
password = os.getenv("PASSWORD")

message = """
Subject:Hello

this is the messenger
you forgot your password
"""

server = smtplib.SMTP("smtp.office365.com",587)
server.starttls()
server.login(server,password)
server.sendmail(sender,receiver,message)
server.quit()

