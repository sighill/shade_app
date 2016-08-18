from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def home(request):
    context={	'style': 'style.css',
    			'main_img': 'main_img_3.jpg',
    			'main_profile': 'main_char_1.jpg',
    			'main_char': 'main_char_1.jpg',
    			'main_github': 'main_github_1.png',
    		}
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context,request))

def account(request):
    context={'style': 'style.css',}
    template = loader.get_template('account.html')
    return HttpResponse(template.render(context,request))