from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime


def combat(request):
    now = datetime.datetime.now()
    return render_to_response('combat.html', {
        'time': now,
    })


def menu(request):
    now = datetime.datetime.now()
    return render_to_response('menu.html', {
        'time': now,
    })