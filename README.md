# email_sender utility

This is an Utility to send email from linux servers. This one is needed because of such utility like s-nail, swaks, heirloom mailx (all can connect directly to  smtp-servers) are absent in AstraLinux 1.7

It works!
to use Gmail you should create an "App Passwords" in your google-account settings (you can not use your gmail password, you will receive 'new' password for your gmail account in the "App Passwords" google-account settings )

email_sender.py  utility able to accept such CLI  keys (utility will ask in interactive mode if required parameters are not set):  
-f (or --fromsender) asks to fill 'From:' field.  
-a (or --addressee) asks to fill  'To:' field.  
-s (or --subject) asks to fill  'Subject:' field.  
-m (or --messagebody) asks to fill Message body filed (text of the email message).  
-S (or --SMTPserver) asks to fill smtp-server dns-name. Will use "hardcoded" value smtp.gmail.com if just Enter hinted.  
-P (or --Port) asks to fill integer value of smtp-server port field. Will use default port 587 if just Enter hinted.  
-l (or --loginsmtp) asks to fill smtp-server login.  
-p (or --passwordsmtp) asks to fill smtp-server  password.  

Usage of full-featured version email_sender.py (example!):
```
# python3 email_sender_cli.py -s emailsubject -m bodymessage -f youremail@gmail.com -a addressee-email@gmail.com -S smtp.gmail.com -P 587 -l youremail@gmail.com -p "yourpasswordhere"
```
OR (You will be asked for a password)
```
# python3 email_sender_cli.py -s emailsubject -m bodymessage -f youremail@gmail.com -a addressee-email@gmail.com -S smtp.gmail.com -P 587 -l youremail@gmail.com 

```
OR (You will be asked for an email subject, email body, and a password)
```
# python3 email_sender_cli.py -f youremail@gmail.com -a addressee-email@gmail.com -S smtp.gmail.com -P 587 -l youremail@gmail.com -p "yourpasswordhere"
```


Usage of legacy version email_sender_interactive.py:
```
# python3 email_sender_interactive.py
```

Usage of legacy version email_sender_interactive.py (example!):
```
# python3 email_sender_cli.py -s emailsubject -m bodymessage -f youremail@gmail.com -a addressee-email@gmail.com -S smtp.gmail.com -P 587 -l youremail@gmail.com -p "yourpasswordhere"
```



bsd-mailx-replace.py  utility able to accept such CLI  keys (utility will ask in interactive mode if required parameters are not set):  
-s (or --subject) asks to fill  'Subject:' field.  
-p (or --passwordsmtp) asks to fill smtp-server  password.  

Variables for bsd-mailx-replace.py  utility  must be set in the /opt/mailsender/variables.ini file
The example of /opt/mailsender/variables.ini content is here:
```
[Settings]
SMTPserver = smtp.gmail.com
Port = 587
sender = youremail@gmail.com
loginsmtp = youremail@gmail.com
passwordsmtp = yourpassword
```

Usage of bsd-mailx_like cli-version bsd-mailx-replace.py:
```
mkdir /opt/mailsender/
vi /opt/mailsender/variables.ini
chmod 600 /opt/mailsender/variables.ini
cp bsd-mailx-replace.py /opt/mailsender/bsd-mailx-replace.py
chmod +x /opt/mailsender/bsd-mailx-replace.py
export PATH=/opt/mailsender:$PATH
ln -s /opt/mailsender/mail /opt/mailsender/bsd-mailx-replace.py

echo "body message" | mail -s 'email subject' addressee-email@gmail.com 

```