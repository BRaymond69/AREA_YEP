from django.contrib import admin

from .models import Service, Facebook, Intra, Twitter, Twitch, News, Netflix, Amazon, Film

# Register your models here.

admin.site.register(Service)
admin.site.register(Facebook)
admin.site.register(Intra)
admin.site.register(Twitter)
admin.site.register(Twitch)
admin.site.register(News)
admin.site.register(Netflix)
admin.site.register(Film)
admin.site.register(Amazon)
