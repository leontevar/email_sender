# email_sender utility

This is an Utility to send email from linux servers. This one is needed because of such utility like s-nail,swaks, heirloom mailx (all can connect directly to  smtp-servers) are absent in AstraLinux 1.7

It works!
to use Gmail you should create an "App Passwords" in your google-account settings


Usage of full-featured version email_sender.py (example!):
```
# python3 email_sender_cli.py -s emailsubject -m bodymessage -f youremail@gmail.com -a addressee-email@gmail.com -S smtp.gmail.com -P 587 -l youremail@gmail.com -p "yourpasswordhere"
```
OR (You will be asked for a password)
```
# python3 email_sender_cli.py -s emailsubject -m bodymessage -f youremail@gmail.com -a addressee-email@gmail.com -S smtp.gmail.com -P 587 -l youremail@gmail.com 

```
OR (You will be asked for a email subject, email body, and a password)
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