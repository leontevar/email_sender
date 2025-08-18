import smtplib
from email.mime.text import MIMEText
from getpass import getpass
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--subject", nargs='?', default="defaultvalue")
parser.add_argument("-m", "--messagebody", nargs='?', default="defaultvalue")
parser.add_argument("-f", "--fromsender", nargs='?', default="defaultvalue")
parser.add_argument("-a", "--addressee", nargs='?', default="defaultvalue")
parser.add_argument("-S", "--SMTPserver", nargs='?', default="defaultvalue")
parser.add_argument("-P", "--Port", nargs='?', default="defaultvalue")
parser.add_argument("-l", "--loginsmtp", nargs='?', default="defaultvalue")
parser.add_argument("-p", "--passwordsmtp", nargs='?', default="defaultvalue")


args = parser.parse_args()



msg = MIMEText(args.messagebody)
msg['Subject'] = args.subject
msg['From'] = args.fromsender
msg['To'] = args.addressee
server = smtplib.SMTP(args.SMTPserver, args.Port)
server.starttls()
server.login(args.loginsmtp,args.passwordsmtp)
server.sendmail(args.fromsender, args.addressee, msg.as_string())
server.quit()
print("E-mail sent")