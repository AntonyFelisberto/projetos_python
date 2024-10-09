import smtplib
import os
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
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

attachment_path = "automation\\email\\file\\tiger (1).jpeg"
attachment_file = open(attachment_path,"rb")
payload = MIMEBase("application","octate-stream")
payload.set_payload(attachment_file.read())
encoders.encode_base64(payload)
payload.add_header("Content-Disposition", "attachment",filename="Image_tiger")
message.attach(payload)

server = smtplib.SMTP("smtp.office365.com",587)
server.starttls()
server.login(server,password)
server.sendmail(sender,receiver,message)
server.quit()