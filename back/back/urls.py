from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from serviceApp.views import ServicesView, FacebookView, IntraView, TwitterView, TwitchView, NewsView, FilmView, AmazonView, NetflixView, testView
from authApp.views import Login, Logout, Register, GoogleRegister, JsonView

from serviceApp.timer import taskManager

urlpatterns = [
    path('admin/', admin.site.urls),

    path('token-gen/', obtain_auth_token, name='api_token_auth'),
    path('login/', Login, name='login'),
    path('register/', Register, name='register'),
    path('googleregister/', GoogleRegister, name='register'),
    path('logout/', Logout, name='logout'),
    path('about.json', JsonView),

    path('services/', ServicesView, name='services'),
    path('facebook/', FacebookView, name='facebook'),
    path('intra/', IntraView, name='intra'),
    path('twitter/', TwitterView, name='twitter'),
    path('twitch/', TwitchView, name='twitch'),
    path('news/', NewsView, name='news'),
    path('film/', FilmView, name='film'),
    path('amazon/', AmazonView, name='amazon'),
    path('netflix/', NetflixView, name='netflix'),
    path('test/', testView, name='test'),
]

taskManager()

# http post http://127.0.0.1:8000/token-gen/ username=enzo password=admin
