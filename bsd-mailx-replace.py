#!/usr/bin/python3

import smtplib
import sys
import argparse
import configparser

from email.mime.text import MIMEText
from getpass import getpass

config = configparser.ConfigParser()
config.read('/opt/mailsender/variables.ini') #config-file

SMTPserver = config["Settings"]["SMTPserver"]
Port = config["Settings"]["Port"]
sender = config["Settings"]["sender"]
loginsmtp = config["Settings"]["loginsmtp"]


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--passwordsmtp", nargs='?')
parser.add_argument("-s", "--subject", nargs='?')
parser.add_argument("recipient") #first non-key positional parameter will be used as an addressee-email

args = parser.parse_args()

if args.passwordsmtp is None:
    if config.has_option("Settings", "passwordsmtp"):
        passwordsmtp = config["Settings"]["passwordsmtp"] #will use field passwordsmtp from config-file
    else:
        passwordsmtp = getpass() #will ask user to input password
else:
    passwordsmtp = args.passwordsmtp

if args.subject is None:
    subject = input("'Subject:' field. Place any text: ")
else:
    subject = args.subject

body = sys.stdin.read() #let us to pass stdin like this:  "echo lalala | bsd-mailx-replace.py"

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = args.recipient

server = smtplib.SMTP(SMTPserver, Port)
server.starttls()
server.login(loginsmtp, passwordsmtp)
server.sendmail(sender, args.recipient, msg.as_string())
server.quit()
print("E-mail sent")