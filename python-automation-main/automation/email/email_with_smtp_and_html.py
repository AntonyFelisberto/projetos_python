import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "YOUR EMAIL"
receiver = "WHO WILL RECEIVE THE EMAIL"
password = os.getenv("PASSWORD")

message = MIMEMultipart()
message["From"] = sender
message["To"] = receiver
message["Subject"] = "Hello stranger"

body = """
<h2>WHAT YOU BUYING</h2>
"""
mimetext = MIMEText(body,"html")
message.attach(mimetext)
message = message.as_string()

server = smtplib.SMTP("smtp.office365.com",587)
server.starttls()
server.login(server,password)
server.sendmail(sender,receiver,message)
server.quit()