from django.db import models

# Create your models here.

class Country(models.Model):
	country_name = models.CharField(max_length=30)	
	continent = models.CharField(max_length=30)
	big = models.BooleanField(default=True)

	def __str__(self):
		return self.country_name

class Capital(models.Model):
	country = models.OneToOneField(Country, on_delete=models.CASCADE, null=True, blank=True)
	capital_name = models.CharField(max_length=30)
	registered_on = models.DateField(null=True,blank=True)

	def __str__(self):
		return self.capital_name