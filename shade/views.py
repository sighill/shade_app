from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def home(request):
    context={'style': 'style.css','main_img': 'main.jpg'}
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context,request))

def account(request):
    context={'style': 'style.css',}
    template = loader.get_template('account.html')
    return HttpResponse(template.render(context,request))