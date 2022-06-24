#!/usr/bin/python3

import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import sys
from datetime import date
from datetime import datetime

"""
    For this service the programme need email adress and his password and subject (objet du mail en fr)
    You got result of request inside dict here : info
    You can encore it in json and do what you want with this
    Programme get last mail 
"""

class Mailer():
    def __init__(self, username="", password=""):
        self.username = username
        self.password = password
        self.imap = imaplib.IMAP4_SSL("imap.gmail.com")
        self.info = {
            "Body": "",
            "Subject" : "",
            "From" : "",
            "Date": "",
            "Since": ""
        }  
        self.return_data = []
    
    def parsing(self, date_mail):
        today = date.today()
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        date_mail = (date_mail[0][0][:-5])
        spliter = date_mail.split(' ')
        day = spliter[1]
        month = spliter[2]
        hour = spliter[4]
        list_month = ["0", 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        day1 = today.strftime("%d")
        month1 = today.strftime("%m")
        if int(month1) <= 9:
            month1 = month1.lstrip('0')
        if int(day) == int(day1):
            y = True
        else:
            y = False
        if month == list_month[int(month1)]:
            z = True
        else:
            z = False
        since = 0
        if y == True and z == True:
            d1 = datetime.strptime(dt_string, '%H:%M:%S')
            d2 = datetime.strptime(hour, '%H:%M:%S')
            since = d1 - d2
        return(date_mail, str(since))
    
    def start(self):
        try:
            self.imap.login(self.username, self.password)
        except:
            return(84)
        status, messages = self.imap.select("INBOX")
        messages = int(messages[0])
        for i in range(messages, messages-1, -1):
            res, msg = self.imap.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    subject, encoding = decode_header(msg["Subject"])[0] # decode the email subject
                    date_mail = decode_header(msg.get("Date")) # decode the email date
                    date_mail, since_date = self.parsing(date_mail)
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding)
                    From, encoding = decode_header(msg.get("From"))[0]
                    if isinstance(From, bytes):
                        From = From.decode(encoding)
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                body = part.get_payload(decode=True).decode() #get the email body
                            except:
                                pass
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                self.info['Body'] = body
                    else: #get the email body
                        content_type = msg.get_content_type() # extract content type of email
                        body = msg.get_payload(decode=True).decode()
                        if content_type == "text/plain":
                            self.info['Body'] = body
                    self.info['Subject'] = subject
                    self.info['From'] = From
                    self.info['Date'] = date_mail
                    self.info['Since'] = since_date
        self.imap.close()
        self.imap.logout()
        return(self.info)
    
    def clean(self, text):
        return "".join(c if c.isalnum() else "_" for c in text)
    
def main():
    try:
        info = Mailer("", "").start()
        print(info)
    except BaseException as error:
        sys.stderr.write(str(type(error).__name__) + ": {}\n".format(error))
if __name__ == "__main__":
    main()
    
