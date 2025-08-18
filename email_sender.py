import smtplib
from email.mime.text import MIMEText
from getpass import getpass
import argparse

default_smtpserver = 'smtp.gmail.com'
default_smtpport = '587'

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--subject", nargs='?')
parser.add_argument("-m", "--messagebody", nargs='?')
parser.add_argument("-f", "--fromsender", nargs='?')
parser.add_argument("-a", "--addressee", nargs='?')
parser.add_argument("-S", "--SMTPserver", nargs='?')
parser.add_argument("-P", "--Port", nargs='?')
parser.add_argument("-l", "--loginsmtp", nargs='?')
parser.add_argument("-p", "--passwordsmtp", nargs='?')


args = parser.parse_args()

#template for me
#if args.XX is None:
#    XX =
#else:
#    XX = args.XX

if args.fromsender is None:
    fromsender = input("'From:' field. Place text like alexander@mail.com: ")
else:
    fromsender = args.fromsender

if args.addressee is None:
    addressee = input("'To:' field. Place text like gigomegoom@mail.com: ")
else:
    addressee = args.addressee

if args.subject is None:
    subject = input("'Subject:' field. Place any text: ")
else:
    subject = args.subject

if args.messagebody is None:
    messagebody = input("Message body filed. Place any text: ")
else:
    messagebody = args.messagebody

if args.SMTPserver is None:
    SMTPserver = input(f"smtp-server dns-name. Place MX-record domain name. If you just hint Enter here  I will use {default_smtpserver}: ") or default_smtpserver
else:
    SMTPserver = args.SMTPserver

if args.Port is None:
    Port = int(input(f"smtp-server port field. Place port here. If you just hint Enter here  I will use default port {default_smtpport}: ") or default_smtpport)
else:
    Port = args.Port

if args.loginsmtp is None:
    loginsmtp = input("smtp-server login: ")
else:
    loginsmtp = args.loginsmtp

if args.passwordsmtp is None:
    passwordsmtp = getpass("smtp-server  password: ")
else:
    passwordsmtp = args.passwordsmtp





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