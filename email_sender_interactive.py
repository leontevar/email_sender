import smtplib
from email.mime.text import MIMEText



fromsender = input("'From:' field. Place text like alexander@mail.com: ")
addressee = input("'To:' field. Place text like gigomegoom@mail.com: ")
subject = input("'Subject:' field. Place any text: ")
message = input("Message body filed. Place any text: ")
SMTPserver = input("smtp-server dns-name. Place MX-record domain name : ")
Port = input("smtp-server port field. Place port here (usually is 587): ")
loginsmtp = input("smtp-server login: ")
passwordsmtp = input("smtp-server  password: ")