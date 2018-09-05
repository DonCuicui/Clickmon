from django.contrib import admin
from .models import Summoner, Clickmon, Attack

@admin.register(Summoner)
class SummonerAdmin(admin.ModelAdmin):
    list_display = ['name','gender', 'money', 'exp']

@admin.register(Clickmon)
class ClickmonAdmin(admin.ModelAdmin):
    list_display = ['hp_max', 'exp', 'img_front']
