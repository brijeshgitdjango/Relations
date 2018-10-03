from django.contrib import admin

# Register your models here.
from .models import Author, Books


class AdminAuthor(admin.ModelAdmin):
	list_display = ['aname', 'age', 'email', 'address']

class AdminBooks(admin.ModelAdmin):
	list_display = ['bname', 'bcost', 'published_on', 'author']

admin.site.register(Author,AdminAuthor)
admin.site.register(Books,AdminBooks)