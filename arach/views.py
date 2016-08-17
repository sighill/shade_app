from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Archetype
# Create your views here.

def arachHome(request):
    context={'style': 'style.css'}
    template = loader.get_template('arach/home.html')
    return HttpResponse(template.render(context,request))

def arachIndex(request):
    characters = Archetype.objects.all()
    template = loader.get_template('arach/index.html')
    context = { 'content':characters ,
                'main_img': 'main.jpg' ,
                'style': 'style.css'
        }
    return HttpResponse(template.render(context , request ))

def arachDisplay(request , character_gid):
    template = loader.get_template('arach/character.html')
    characters = Archetype.objects.all()
    character = Archetype.objects.get(gid = character_gid)
    attribute_list = ['Puissance','Vigueur','Agilité','Perception','Charisme','Astuce','Volonté','Intelligence','Connaissance']
    cast_verbose = character.cast_choice[character.cast-1][1]
    context = { 'content':characters ,
                'avatar': character.img ,
                'description': character.description ,
                'name': character.name ,
                'cast': 'caste des {}'.format(cast_verbose) ,
                'attributes':character.attributes.split(',') ,
                'stuff': character.stuff.split(',') ,
                'style': 'style.css'
                }
    return HttpResponse(template.render(context , request ))


