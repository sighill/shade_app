from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Archetype
# Create your views here.

def arachIndex(request):
    characters = Archetype.objects.all()
    template = loader.get_template('arach/index.html')
    if request.user.is_authenticated():
        current_user = '<a href="/account">{} : gérer son compte</a>'.format(request.user)
    else:
        current_user = '<a href="/login">Se connecter</a>'
    context = { 'content':characters ,
                'style': 'style.css',
                'current_user': current_user,
                'favicon': 'favicon.ico'
            }
    return HttpResponse(template.render(context , request ))

def arachDisplay(request , character_gid):
    template = loader.get_template('arach/character.html')
    characters = Archetype.objects.all()
    character = Archetype.objects.get(gid = character_gid)
    if request.user.is_authenticated():
        current_user = '<a href="/account">{} : gérer son compte</a>'.format(request.user)
    else:
        current_user = '<a href="/login">Se connecter</a>'
    attribute_list = ['Puissance','Vigueur','Agilité','Perception','Charisme','Astuce','Volonté','Intelligence','Connaissance']
    cast_verbose = character.cast_choice[character.cast-1][1]
    context = { 'content':characters ,
                'avatar': character.img ,
                'description': character.description ,
                'name': character.name ,
                'cast': 'caste des {}'.format(cast_verbose) ,
                'attributes':character.attributes.split(',') ,
                'stuff': character.stuff.split(',') ,
                'style': 'style.css',
                'current_user': current_user,
                'favicon': 'favicon.ico'
            }
    return HttpResponse(template.render(context , request ))


