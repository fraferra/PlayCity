from django.contrib import admin
from city.models import *
from django.contrib.auth.models import User


class CityAdmin(admin.ModelAdmin):
	model=City
	fields=['name','latitude', 'longitude']



admin.site.register(City, CityAdmin) 

