from django.contrib import admin

# Register your models here.

from .models import Country, Capital

class AdminCountry(admin.ModelAdmin):
	list_display = ['country_name','continent','big']

class AdminCapital(admin.ModelAdmin):
	list_display = ['capital_name','registered_on', 'country']

admin.site.register(Country, AdminCountry)
admin.site.register(Capital, AdminCapital)
