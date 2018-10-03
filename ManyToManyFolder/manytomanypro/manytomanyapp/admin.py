from django.contrib import admin

# Register your models here.
from .models import Game, Person

class AdminGame(admin.ModelAdmin):
	list_display = [ 'gname', 'no_of_players']

class AdminPerson(admin.ModelAdmin):
	list_display = ['pname', 'DOB']


admin.site.register(Person, AdminPerson)
admin.site.register(Game,AdminGame)