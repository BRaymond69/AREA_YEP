from django.contrib.auth.models import User

from request_area.Action.facebook import Facebook as facebookAPI
from request_area.Action.intra_epitech import Intra as intraAPI
from request_area.Action.twitter import Twitter as twitterAPI
from request_area.Action.twitch import Twitch as twitchAPI
from request_area.Action.news import News as newsAPI
from request_area.Action.amazon_prime import Amazon_video as amazonAPI
from request_area.Action.netflix import Netflix as netflixAPI
from request_area.Action.film import Film as filmAPI


from request_area.Reaction.mail_sender import Mail_send as mailSender

from serviceApp.models import Service
import tweepy
import sys

# Create your views here.


#def FacebookJob():
#    serv = Service.objects.all()
#    
#    for i in serv:
#        if serv[i].facebook == None:
#            return()
#        else:
#            email = serv[i].facebook.email
#            password = serv[i].facebook.password
#
#            fbRequest = facebookAPI(email, password)
#            data = fbRequest.start()
#            info = fbRequest.parsing(data)


def IntraJob():
    serv = Service.objects.all()
    for i in range(len(serv)):
        if serv[i].intra != None:
            intraToken = serv[i].intra.autoToken
            name = serv[i].user
            user = User.objects.get(username=name)

            intraRequest = intraAPI(intraToken)            
            data = intraRequest.getNotification(0)["Last notif"]
            if data != serv[i].intra.lastNotif:
                mail = mailSender(user.email)
                mail.start(data)
                serv[i].intra.lastNotif = data
                serv[i].intra.save()

def GradeJob():
    serv = Service.objects.all()
    
    for i in range(len(serv)):
        if serv[i].intra != None:
            intraToken = serv[i].intra.autoToken
            name = serv[i].user
            user = User.objects.get(username=name)

            intraRequest = intraAPI(intraToken)            
            gradeA = float(intraRequest.getNotification(0)["Grade A"])
            gradeB = float(intraRequest.getNotification(0)["Grade B"])
            gradeC = float(intraRequest.getNotification(0)["Grade C"])
            gradeD = float(intraRequest.getNotification(0)["Grade D"])
            gradeE = float(intraRequest.getNotification(0)["Grade E"])
            grades = [gradeA, gradeB, gradeC, gradeD, gradeE]
            if gradeA != serv[i].intra.gradeA or gradeB != serv[i].intra.gradeB or gradeC != serv[i].intra.gradeC or \
            gradeD != serv[i].intra.gradeD or gradeE != serv[i].intra.gradeE:
                mail = mailSender(user.email)
                mail.start(str(grades))
                serv[i].intra.gradeA = float(intraRequest.getNotification(0)["Grade A"])
                serv[i].intra.gradeB = float(intraRequest.getNotification(0)["Grade B"])
                serv[i].intra.gradeC = float(intraRequest.getNotification(0)["Grade C"])
                serv[i].intra.gradeD = float(intraRequest.getNotification(0)["Grade D"])
                serv[i].intra.gradeE = float(intraRequest.getNotification(0)["Grade E"])
                serv[i].intra.save()

def NewsJob():
    serv = Service.objects.all()

    for i in range(len(serv)):
        if serv[i].news != None:
            newsQuery = serv[i].news.newsPaper
            name = serv[i].user
            user = User.objects.get(username=name)

            newsRequest = newsAPI()
            data = newsRequest.start(key_word=newsQuery)
            if data[0]['Description'] != serv[i].news.description:
                mail = mailSender(user.email)
                mail.start(data[0]['Description'])
                serv.news.source = data[0]['Source']
                serv.news.title = data[0]['Title']
                serv.news.description = data[0]['Description']
                serv.news.save()

def TwitterJob():
    serv = Service.objects.all()

    for i in range(len(serv)):
        if serv[i].twitter != None:
            twitterUser = serv[i].twitter.twitterAccount
            info = twitterAPI(twitterUser).start()
            data = info
            if data['Text'] != serv[i].twitter.lastNotif:
                Twitter_post().start(data['Text'])
                serv[i].twitter.lastNotif = data["Text"]
                serv[i].twitter.save()

def TwitchJob():
    serv = Service.objects.all()

    for i in range(len(serv)):
        if serv[i].twitch != None:
            account = serv[i].twitch.twitchAccount
            name = serv[i].user
            user = User.objects.get(username=name)

            intraRequest = twitchAPI()
            data = intraRequest.start(account)
            if data["live title"] != serv[i].twitch.title:
                mail = mailSender(user.email)
                mail.start(data["live title"])
                serv[i].twitch.title = data["live title"]
                serv[i].twitch.playing = data["play"]
                serv[i].twitch.save()


def FilmJob():
    serv = Service.objects.all()

    for i in range(len(serv)):
        if serv[i].film != None:
            filmQuery = serv[i].film.filmNumber
            name = serv[i].user
            user = User.objects.get(username=name)

            filmRequest = filmAPI()
            data = filmRequest.start(number=filmQuery)

            if data["Film"][0] != serv[i].film.title:
                mail = mailSender(user.email)
                mail.start(data["Film"])
                serv.film.title = data["Film"][0]
                serv.film.date = data["Date sortie"][0]
                serv.film.save()

def AmazonJob():
    serv = Service.objects.all()

    for i in range(len(serv)):
        if serv[i].amazon != None:
            name = serv[i].user
            user = User.objects.get(username=name)

            amazonRequest = amazonAPI()
            data = amazonRequest.start(number="last")

            if data != serv[i].amazon.title:
                mail = mailSender(user.email)
                mail.start(data)
                serv.amazon.title = data
                serv.amazon.save()

def NetflixJob():
    serv = Service.objects.all()

    for i in range(len(serv)):
        if serv[i].netflix != None:
            name = serv[i].user
            user = User.objects.get(username=name)

            request = netflixAPI()
            data = request.start(number="last")

            if data != serv[i].netflix.title:
                mail = mailSender(user.email)
                mail.start(data)
                serv.netflix.title = data
                serv.netflix.save()


class Twitter_post():
    def __init__(self, consumer_key='uOqKfFeAD6lZVyra4dlNUSJib', consumer_secret='reUIqFgZ0rqPd6K3xqN49WNHi2LU4bXOvYS8GvYnxthvhBng1x',
    access_token = '882246392575610880-SFY3HIh3JmDV4ucoyRshcdJoprEwsP4', access_token_secret = 'TC23VoJ75ZsM7PIfD5eakXngIhSy3vzSXt9ndrM2qiZab'):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret 
        self.access_token = access_token 
        self.access_token_secret = access_token_secret

    def start(self, sentence = "Hello is my API TEST for AREA an Epitech Project"):
        try:
            auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
            auth.set_access_token(self.access_token, self.access_token_secret)
        except:
            return(84)
        api = tweepy.API(auth)
        api.update_status(sentence)