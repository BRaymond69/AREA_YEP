from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Service, Facebook, Intra, Twitter, Twitch, News, Film, Netflix, Amazon

from request_area.Action.facebook import Facebook as facebookAPI
from request_area.Action.intra_epitech import Intra as intraAPI
from request_area.Action.twitter import Twitter as twitterAPI
from request_area.Action.twitch import Twitch as twitchAPI
from request_area.Action.news import News as newsAPI
from request_area.Action.amazon_prime import Amazon_video as amazonAPI
from request_area.Action.netflix import Netflix as netflixAPI
from request_area.Action.film import Film as filmAPI

# Create your views here.

from django.contrib.auth.models import User
from request_area.Reaction.mail_sender import Mail_send as mailSender
from request_area.Reaction.twitter import Twitter_post as tweetSender

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def testView(request):
    serv = Service.objects.all()
    
    for i in range(len(serv)):
        if serv[i].intra == None:
            return()
        else:
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
    return Response({"data": "info"}, status=status.HTTP_200_OK)

def getUserName(request):
    token = request.headers["Authorization"].split()[1]
    tokenQuery = Token.objects.filter(key__exact=token)

    name = tokenQuery.values("user__username")[0]["user__username"]
    
    return(name)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def ServicesView(request):
    name = getUserName(request)
    serv = Service.objects.get(user__exact=name)

    services = [serv.facebook, serv.intra, serv.twitter, serv.twitch, serv.news, serv.film, serv.amazon, serv.netflix]
    servicesNames = ['facebook', 'intra', 'twitter', 'twitch', 'news', 'film', 'amazon', 'netflix']
    data = {}
    for i in range(len(services)):
        if services[i] != None:
            data.update({servicesNames[i]:True})
        else:
            data.update({servicesNames[i]:False})

    return Response({"data": data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def FacebookView(request):
    name = getUserName(request)

    serv = Service.objects.get(user__exact=name)

    fbEmail = request.data.get("email")
    fbPassword = request.data.get("password")


    if serv.facebook == None and fbPassword != None and fbEmail != None: # If not created creates an instance
        serv.facebook = Facebook.objects.create(email=fbEmail, password=fbPassword)
        serv.save()
    
    if serv.facebook != None and fbPassword != None and fbEmail != None: # If instance allready created changes password and email
        oldData = serv.facebook
        oldData.email = fbEmail
        oldData.password = fbPassword
        oldData.save()

    if serv.facebook == None:
        return Response({"data": "no password or email in database"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Query to Facebook

    serv = Service.objects.get(user__exact=name)
    email = serv.facebook.email
    password = serv.facebook.password

    fbRequest = facebookAPI(email, password)
    data = fbRequest.start()
    info = fbRequest.parsing(data)

    return Response({"data": info}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def IntraView(request): ## Bonne gestion d'erreur
    name = getUserName(request)
    serv = Service.objects.get(user__exact=name)
    autoToken = request.data.get("autoToken")
    intraRequest = intraAPI(autoToken)
    data = intraRequest.getNotification(0)
    if data == 84:
        return Response({"data": "invalit intra token"}, status=status.HTTP_400_BAD_REQUEST)

    if serv.intra == None and autoToken != None:
        serv.intra = Intra.objects.create(autoToken=autoToken)
        serv.save()
    
    if serv.intra != None and autoToken != None:
        oldData = serv.intra
        oldData.autoToken = autoToken
        oldData.save()
    
    if serv.intra == None:
        return Response({"data": "no intra token in database"}, status=status.HTTP_400_BAD_REQUEST)

    serv = Service.objects.get(user__exact=name)
    serv.intra.lastNotif = data["Last notif"]
    serv.intra.gradeA = float(data["Grade A"])
    serv.intra.gradeB = float(data["Grade B"])
    serv.intra.gradeC = float(data["Grade C"])
    serv.intra.gradeD = float(data["Grade D"])
    serv.intra.gradeE = float(data["Grade E"])
    
    ## Chopper les grades
    serv.intra.save()
    return Response({"data": data["Last notif"]}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def TwitterView(request): ## Bonne gestion d'erreur
    name = getUserName(request)

    serv = Service.objects.get(user__exact=name)

    twitterAccount = request.data.get("twitterAccount")

    twitterRequest = twitterAPI(twitterAccount)
    data = twitterRequest.start()
    if data == 84:
        return Response({"data": "invalit twitter user"}, status=status.HTTP_400_BAD_REQUEST)

    if serv.twitter == None and twitterAccount != None:
        serv.twitter = Twitter.objects.create(twitterAccount=twitterAccount)
        serv.save()
    
    if serv.twitter != None and twitterAccount != None:
        oldData = serv.twitter
        oldData.twitterAccount = twitterAccount
        oldData.save()
    
    if serv.twitter == None:
        return Response({"data": "no Twitter data in database"}, status=status.HTTP_400_BAD_REQUEST)
    
    serv = Service.objects.get(user__exact=name)
    serv.twitter.lastNotif = data["Text"]
    serv.save()

    return Response({"data": data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def TwitchView(request): ## Bonne gestion d'erreur
    name = getUserName(request)

    serv = Service.objects.get(user__exact=name)

    twitchAccount = request.data.get("twitchAccount")

    twitchRequest = twitchAPI()
    data = twitchRequest.start(twitchAccount)

    if data == None:
        return Response({"data": "invalid twitch account"}, status=status.HTTP_400_BAD_REQUEST)
    
    if serv.twitch == None and twitchAccount != None:
        serv.twitch = Twitch.objects.create(twitchAccount=twitchAccount)
        serv.save()
    
    if serv.twitch != None and twitchAccount != None:
        oldData = serv.twitch
        oldData.twitchAccount = twitchAccount
        oldData.save()
    
    if serv.twitch == None:
        return Response({"data": "no twitch data in database"}, status=status.HTTP_400_BAD_REQUEST)
    
    serv = Service.objects.get(user__exact=name)
    serv.twitch.title = data["live title"]
    serv.twitch.playing = data["play"]
    serv.twitch.save()
    return Response({"data": data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def NewsView(request): ## Bonne gestion d'erreur
    name = getUserName(request)
    serv = Service.objects.get(user__exact=name)
    newsQuery = request.data.get("newsPaper")

    newsRequest = newsAPI()
    data = newsRequest.start(key_word=newsQuery)
    if data == 84:
        return Response({"data": "no news"}, status=status.HTTP_400_BAD_REQUEST)

    if serv.news == None and newsQuery != None:
        serv.news = News.objects.create(newsPaper=newsQuery)
        serv.save()
    
    if serv.news != None and newsQuery != None:
        oldData = serv.news
        oldData.newsPaper = newsQuery
        oldData.save()
    
    if serv.news == None:
        return Response({"data": "no news data in database"}, status=status.HTTP_400_BAD_REQUEST)

    serv = Service.objects.get(user__exact=name)
    if len(data) > 1:
        serv.news.source = data[0]['Source']
        serv.news.title = data[0]['Title']
        serv.news.description = data[0]['Description']
        serv.news.save()
    return Response({"data": data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def FilmView(request): ## Bonne gestion d'erreur
    name = getUserName(request)

    serv = Service.objects.get(user__exact=name)

    filmNumber = request.data.get("filmNumber")

    filmRequest = filmAPI()
    data = filmRequest.start(number=filmNumber)

    if len(data["Film"]) == 0 or filmNumber.isdigit() == False:
        return Response({"data": "invalid entry or no film"}, status=status.HTTP_400_BAD_REQUEST)

    if serv.film == None and filmNumber != None:
        serv.film = Film.objects.create(filmNumber=filmNumber)
        serv.save()
    
    if serv.film != None and filmNumber != None:
        oldData = serv.film
        oldData.filmNumber = int(filmNumber)
        oldData.save()
    
    serv = Service.objects.get(user__exact=name)

    # get le prochain film a sortir
    serv.film.title = data["Film"][0]
    serv.film.date = data["Date sortie"][0]
    serv.film.save()

    return Response({"data": data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def AmazonView(request): ## Bonne gestion d'erreur
    name = getUserName(request)

    serv = Service.objects.get(user__exact=name)

    amazonRequest = amazonAPI()
    data = amazonRequest.start(number="last")

    if data == "":
        return Response({"data": "no film"}, status=status.HTTP_400_BAD_REQUEST)

    if serv.amazon == None:
        serv.amazon = Amazon.objects.create()
        serv.save()
    
    serv = Service.objects.get(user__exact=name)
    serv.amazon.title = data
    serv.amazon.save()

    return Response({"data": data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def NetflixView(request): ## Bonne gestion d'erreur
    name = getUserName(request)

    serv = Service.objects.get(user__exact=name)

    request = netflixAPI()
    data = request.start(number="last")

    if data == "":
        return Response({"data": "no film"}, status=status.HTTP_400_BAD_REQUEST)

    if serv.netflix == None:
        serv.netflix = Netflix.objects.create(title=data)
        serv.save()
    
    serv = Service.objects.get(user__exact=name)
    serv.netflix.title = data
    serv.netflix.save()

    return Response({"data": data}, status=status.HTTP_200_OK)