#!/usr/bin/python3

import smtplib
import sys
sys.path.append('../Action')
from request_area.Action.twitch import Twitch
from request_area.Action.film import Film
from request_area.Action.news import News


"""
    Needed stmplib
    How work script : you need to call start with your personnel message et set the mail of receiver
    If you want access to notif with e-mail, you call start function with second argument initalize to False
    !!!!! BE CAREFUUL don't use : in your message, otherwise you will receive empty mail
    example just for send mail:
        Mail_send("exemple@gmail.com").start("Hello ! how were you man !")
    example for notif:
        Mail_send(""exemple@gmail.com").start(value=False)

"""

class Mail_send():
    def __init__(self, youremail = ""):
        self.email = "area.2k21.epitechlyon@gmail.com"
        self.password = "_Epitech2k21_"
        self.dest = youremail
    
    def start(self, message="Hello it's AREA project from EPITECH", value=True):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        try:
            s.login(self.email, self.password)
        except:
            return(84)
        info = Twitch().start()
        if value == False:
            if info['is_live'] == True:
                message_twitch = str("Your favorite streamer " + info['Streamer'] + " is in live, his/her play " 
                                    + info['play'] + " Title " + info['live title'].replace("é", 'e').replace('à', 'a').replace('è', 'e') 
                                    + " Stream begin at " +info['Start at'][11:-1].replace(":", " "))
                s.sendmail(self.email, self.dest, message_twitch)
            return_message = ""
            info2 = Film().start()
            for i in range(len(info2['J-'])):
                if int(info2['J-'][i]) <=  7:
                    film = str(info2['Film'][i]).replace('à', 'a')
                    return_message = "Your film "+ film +" is coming soon in " + str(info2['J-'][i]) + " days " + "(" + info2["Date sortie"][i] + ")"
                    s.sendmail(self.email, self.dest, return_message)
            info3 = News().start()
            return_message_news = []
            for i in range(len(info3)):
                if bool(info3[i]['Recent']) ==  True:
                    message_news = info3[i]['Source'] + " has pusblished " + info3[i]['Title'] + " it's " + info3[i]['Description'] + " if want check the article with this url go type title of article in google"
                    return_message_news.append(message_news)
                    s.sendmail(self.email, self.dest, str(return_message_news))
                else:
                    message_news = info3[i]['Source'] + " has pusblished " + info3[i]['Title'] + " it's " + info3[i]['Description'] + " if want check the article with this url go type title of article in google"
                    s.sendmail(self.email, self.dest, message_news)
        else:
            s.sendmail(self.email, self.dest, message)
        s.quit()

def main():
    try:
        Mail_send().start()
    except BaseException as error:
        sys.stderr.write(str(type(error).__name__) + ": {}\n".format(error))

if __name__ == "__main__":
    main()