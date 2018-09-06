from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from .models import Summoner, Clickmon, Attack, AttackPack
import random

def combat(request, clickmon_id):
    clickmon = Clickmon.objects.get(id=clickmon_id)
    return render_to_response('combat.html', {
        'clickmon': clickmon,
        # 'Attack': Attack,
        # 'AttackPack':AttackPack,
        # 'Summoner': Summoner,

    })


def menu(request):
    summoner, created = Summoner.objects.get_or_create(name='alban', mdp='gfkjlknl')
    return render_to_response('menu.html', {
        'summoner': summoner,
    })


