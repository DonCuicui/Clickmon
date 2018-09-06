from django.contrib import admin
from .models import Summoner, Clickmon, Attack, AttackPack

@admin.register(Summoner)
class SummonerAdmin(admin.ModelAdmin):
    list_display = ['name','gender', 'money', 'exp']

@admin.register(Clickmon)
class ClickmonAdmin(admin.ModelAdmin):
    list_display = ['name', 'summoner', 'hp_max', 'damage', 'stamina_max', 'element', 'exp', 'img_front', 'img_back',
                    'level']

@admin.register(Attack)
class AttackAdmin(admin.ModelAdmin):
    list_display = ['name','element','stamina_cost', 'img', 'damage']

@admin.register(AttackPack)
class AttackPackAdmin(admin.ModelAdmin):
    list_display = ['Clickmon', 'attack_one', 'exp_one', 'attack_two', 'exp_two', 'attack_three', 'exp_three',
                    'attack_four', 'exp_four']
