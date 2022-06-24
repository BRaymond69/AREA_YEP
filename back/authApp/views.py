import time

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from serviceApp.models import Service

import requests
from .serializer import RegisterSerializer, UserSerializer

# Create your views here.

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def Register(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    Service.objects.create(user=user)
    return Response({"data": UserSerializer(user).data}, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def GoogleRegister(request):
    if request.data["googleToken"] == None:
        return Response({"data": "No google token given"}, status=status.HTTP_400_BAD_REQUEST)
    token = request.data["googleToken"]
    data = requests.get('https://oauth2.googleapis.com/tokeninfo?id_token=' + token)
    
    username = data.json()["name"].replace(" ", "_")
    email = data.json()["email"]
    password = data.json()["email"]

    user = authenticate(username=username, password=password)

    if not user:
        info = {
            'username': username,
            'email': email,
            'password': password
        }
        serializer = RegisterSerializer(data=info)
        serializer.is_valid(raise_exception=True)
        user = serializer.save() ## Create user

        Service.objects.create(user=user)
        user = authenticate(username=username, password=password) ## Login user
        token, _ = Token.objects.get_or_create(user=user)
        returnInfo = {
            'token' : token.key,
            'username': username,
            'email': email,
        }
        return Response(returnInfo, status=status.HTTP_201_CREATED)

    token, _ = Token.objects.get_or_create(user=user)
    user = User.objects.filter(username__exact=username)
    email = user.values("email")[0]["email"]
    return Response({
        'token': token.key,
        'username': username,
        'email': email
    }, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def Login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response({'error': 'username/password not entered'}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'username/password not found'}, status=status.HTTP_400_BAD_REQUEST)
    token, _ = Token.objects.get_or_create(user=user)

    user = User.objects.filter(username__exact=username)
    email = user.values("email")[0]["email"]
    return Response({
        'token': token.key,
        'username': username,
        'email': email
    }, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def Logout(request):
    token = request.headers["Authorization"].split()[1]

    print(token)
    token = Token.objects.get(key__exact=token)
    token.delete()
    return Response({'data': 'You logged out successfully'}, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
@permission_classes((AllowAny,))
def JsonView(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    data = {
        "client": {
            "host": ip
        },
        "server": {
            "current_time": int(time.time() + 28800),
            "services": [{
                "name": "intra",
                "actions": [{
                    "name": "new_notification",
                    "description": "Gets latest notification"
                }, {
                    "name": "news_grade",
                    "description": "Gets new grade from the intra"
                }],
                "reactions": [{
                    "name": "sends_email",
                    "description": "sends an email to user's inbox"
                }]
            }, {
                "name": "facebook",
                "actions": [{
                    "name": "message",
                    "description": "Get the last message recieved"
                }],
                "reactions": [{
                    "name": "send_message",
                    "description": "Sends an message to user's inbox"
                }]
            }, {
                "name": "film",
                "actions": [{
                    "name": "latest_film",
                    "description": "Gets the latest film"
                }],
                "reactions": [{
                    "name": "sends_email",
                    "description": "Sends an email to user's inbox"
                }]
            }, {
                "name": "netflix",
                "actions": [{
                    "name": "get_film",
                    "description": "Get the last film or serie on netflix platform"
                }],
                "reactions": [{
                    "name": "sends_email",
                    "description": "Sends an email to user's inbox"
                }]
            }, {
                "name": "twitter",
                "actions": [{
                    "name": "latest_tweet",
                    "description": "Gets specified user's latest tweet"
                }],
                "reactions": [{
                    "name": "tweet_send",
                    "description": "Sends a tweet in response"
                }]
            }, {
                "name": "news",
                "actions": [{
                    "name": "get_news",
                    "description": "Get the news about a subject"
                }],
                "reactions": [{
                    "name": "sends_email",
                    "description": "Sends an email to user's inbox"
                }]
            }, {
                "name": "amazon",
                "actions": [{
                    "name": "latest_prime_episode",
                    "description": "Gets latest amazon prime episode"
                }],
                "reactions": [{
                    "name": "sends_email",
                    "description": "Sends an email to user's inbox"
                }]
            }, {
                "name": "date",
                "actions": [{
                    "name": "today's_date",
                    "description": "current day and time"
                }],
                "reactions": [{
                    "name": "sends_email",
                    "description": "Sends an email to user's inbox"
                }]
            }, {
                "name": "mail",
                "actions": [{
                    "name": "mail_getter",
                    "description": "Get the last mail received"
                }],
                "reactions": [{
                    "name": "sends_email",
                    "description": "Sends an email to user's inbox"
                }]
            }, {
                "name": "twitch",
                "actions": [{
                    "name": "twitch_streamer",
                    "description": "watches if a streamer is live"
                }],
                "reactions": [{
                    "name": "sends_email",
                    "description": "Sends an email to user's inbox"
                }]
            }],
        }
    }
    return Response(data, status=status.HTTP_200_OK)
