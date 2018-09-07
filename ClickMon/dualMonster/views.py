from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect

from .models import Summoner, Clickmon, Attack, AttackPack
import random, requests

def get_summoner():
    return Summoner.objects.get_or_create(name='El Cuicui', mdp='Patate')[0]

def new_clickmon(request):
    first_int = random.randint(1, 151)
    second_int = random.randint(1, 151)
    clickmon_exp = random.randint(1, 1000)
    clickmon_name = request.GET.get('name', 'monstre')
    clickmon_hp_max = random.randint(50, 500)
    clickmon_element = 'normal'
    clickmon_stamina_max = random.randint(5, 50)
    clickmon_damage =random.randint(5, 50)
    image_url = f'http://images.alexonsager.net/pokemon/fused/{first_int}/{first_int}.{second_int}.png'
    image_content= requests.get(image_url).content
    image=ContentFile(image_content, name= f'{first_int}-{first_int}-{second_int}.png')
    clickmon = Clickmon.objects.get_or_create(
                                    summoner= get_summoner(),
                                    img_front=image,
                                    img_back=image,
                                    exp= clickmon_exp,
                                    name =clickmon_name,
                                    hp_max =  clickmon_hp_max,
                                    element= clickmon_element,
                                    stamina_max =clickmon_stamina_max,
                                    damage =clickmon_damage)
    return redirect('menu')

def combat(request, clickmon_id):
    clickmon = Clickmon.objects.get(id=clickmon_id)

    clickmon_ennemy = Clickmon.objects.order_by('?')[0]


    return render_to_response('combat.html', {
        'clickmon': clickmon,
        'clickmon_ennemy': clickmon_ennemy,
    })


def menu(request):
    return render_to_response('menu.html', {
        'summoner': get_summoner(),
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
