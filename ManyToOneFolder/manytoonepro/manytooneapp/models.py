from django.db import models

# Create your models here.
class Author(models.Model):
	aname = models.CharField(max_length=30)
	age = models.IntegerField()
	address = models.CharField(max_length=30)
	email = models.EmailField(default="abc@gmail.com")

	def __str__(self):
		return self.aname
	

class Books(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
	bname = models.CharField(max_length=50)
	bcost = models.IntegerField(null=True, blank=True)
	published_on = models.DateField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.bname