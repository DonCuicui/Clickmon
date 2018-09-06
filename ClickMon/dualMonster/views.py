from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from .models import Summoner, Clickmon, Attack, AttackPack


def combat(request, clickmon_id):
    clickmon = Clickmon.objects.get(id=clickmon_id)

    clickmon_ennemy = Clickmon.objects.order_by('?')[0]


    return render_to_response('combat.html', {
        'clickmon': clickmon,
        'clickmon_ennemy': clickmon_ennemy,
    })


def menu(request):
    summoner, created = Summoner.objects.get_or_create(name='alban', mdp='gfkjlknl')
    return render_to_response('menu.html', {
        'summoner': summoner,
    })


def attack(request, clickmon_id, clickmon_ennemy_id):
    clickmon = Clickmon.objects.get(id=clickmon_id)
    clickmon_ennemy = Clickmon.objects.get(id=clickmon_ennemy_id)

    # calcul du combat puis enregistrement des nouvelles donnees dans la base

    clickmon.attack(clickmon_ennemy)

    return render_to_response('attack.html', {
        'clickmon': clickmon,
        'clickmon_ennemy': clickmon_ennemy,
    })

    # une fois tester le bon fonctionnement de la fonction attack de la class Clickmon du models
    # url = '/combat/' + str(clickmon.id)
    # return redirect(url)
