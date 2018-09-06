from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from .models import Summoner, Clickmon, Attack, AttackPack


def combat(request):
    now = datetime.datetime.now()
    return render_to_response('combat.html', {
        'time': now,
        'Clickmon': Clickmon,
        'Attack': Attack,
        'AttackPack':AttackPack,
        'Summoner': Summoner,


    })


def menu(request):
    now = datetime.datetime.now()
    return render_to_response('menu.html', {
        'time': now,
    })


