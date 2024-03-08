##
#
#uvoo uoke qpvo ytba 
import smtplib, ssl
from email.message import EmailMessage

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "sandakovroman2@gmail.com"
password = input("Type your password and press enter")
#Create a secure SSL context
context = ssl.create_default_context()
msg = EmailMessage()
msg.set_content("Tere")
msg['Subject']="Kirja teema"
msg['From']="sandakovroman2@gmail.com"
msg['To']="marina.oleinik@tthk.ee"

#msg="Tere tulemast!"
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.send_message(msg)
except Exception as e:
    print(e)
finally:
    server.quit()