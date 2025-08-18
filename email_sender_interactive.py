import smtplib
from email.mime.text import MIMEText
from getpass import getpass

default_smtpserver = 'smtp.gmail.com'
default_smtpport = '587'

fromsender = input("'From:' field. Place text like alexander@mail.com: ")
addressee = input("'To:' field. Place text like gigomegoom@mail.com: ")
subject = input("'Subject:' field. Place any text: ")
messagebody = input("Message body filed. Place any text: ")
SMTPserver = input(f"smtp-server dns-name. Place MX-record domain name. If you just hint Enter here  I will use {default_smtpserver}: ") or default_smtpserver
Port = int(input(f"smtp-server port field. Place port here. If you just hint Enter here  I will use default port {default_smtpport}: ") or default_smtpport)
loginsmtp = input("smtp-server login: ")
passwordsmtp = getpass("smtp-server  password: ")

msg = MIMEText(messagebody)
msg['Subject'] = subject
msg['From'] = fromsender
msg['To'] = addressee
server = smtplib.SMTP(SMTPserver, Port)
server.starttls()
server.login(loginsmtp,passwordsmtp)
server.sendmail(fromsender, addressee, msg.as_string())
server.quit()
print("E-mail sent")