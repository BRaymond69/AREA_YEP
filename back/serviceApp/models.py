from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Facebook(models.Model):
    email = models.EmailField(blank=True, null=True)
    password = models.TextField(max_length=256, blank=True, null=True)

class Intra(models.Model):
    autoToken = models.TextField(max_length=256, blank=True, null=True)
    lastNotif = models.TextField(blank=True, null=True) ###
    gradeA = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    gradeB = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    gradeC = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    gradeD = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    gradeE = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    
class Twitter(models.Model):
    twitterAccount = models.TextField(max_length=256, blank=True, null=True)
    lastNotif = models.TextField(blank=True, null=True) ###
    
class Twitch(models.Model):
    twitchAccount = models.TextField(max_length=256, blank=True, null=True)
    title = models.TextField(blank=True, null=True) ###
    playing = models.TextField(blank=True, null=True) ###

class News(models.Model):
    newsPaper = models.TextField(max_length=256, blank=True, null=True)
    source = models.TextField(blank=True, null=True) ###
    title = models.TextField(blank=True, null=True) ###
    description = models.TextField(blank=True, null=True) ###

class Film(models.Model):
    filmNumber = models.IntegerField()
    title = models.TextField(blank=True, null=True) ###
    date = models.TextField(blank=True, null=True) ###

class Netflix(models.Model):
    title = models.TextField(blank=True, null=True) ###

class Amazon(models.Model):
    title = models.TextField(blank=True, null=True) ###

class Service(models.Model):
    user = models.CharField(max_length=256)
    facebook = models.ForeignKey(Facebook, on_delete=models.CASCADE, blank=True, null=True)
    intra = models.ForeignKey(Intra, on_delete=models.CASCADE, blank=True, null=True)
    twitter = models.ForeignKey(Twitter, on_delete=models.CASCADE, blank=True, null=True)
    twitch = models.ForeignKey(Twitch, on_delete=models.CASCADE, blank=True, null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, blank=True, null=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, blank=True, null=True)
    netflix = models.ForeignKey(Netflix, on_delete=models.CASCADE, blank=True, null=True)
    amazon = models.ForeignKey(Amazon, on_delete=models.CASCADE, blank=True, null=True)
