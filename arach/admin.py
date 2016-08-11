from django.contrib import admin
from .models import Archetype

# Register your models here.

class adminArchetype(admin.ModelAdmin):
	list_display = ['gid','img', 'name','description','age','cast',
		'attributes']
	ordering = ['gid']

admin.site.register(Archetype , adminArchetype)