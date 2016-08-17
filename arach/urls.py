# urls.py
from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^character/(?P<character_gid>\d+)', views.arachDisplay, name='Character'),
    url(r'^$' , views.arachIndex),
]