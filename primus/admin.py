from django.contrib import admin
from .models import FirstName , LastName

# Register your models here.

class detailFirstName(admin.ModelAdmin):
	list_display = ['uid', 'name', 'genre', 'origin', 'use_count']
	ordering = ['uid']

admin.site.register(FirstName , detailFirstName)