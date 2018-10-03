from django.db import models



class Person(models.Model):
	pname = models.CharField(max_length=30)
	DOB = models.DateField()

	def __str__(self):
		return self.pname


class Game(models.Model):
	person = models.ManyToManyField(Person)
	gname = models.CharField(max_length=50)
	no_of_players = models.IntegerField(default=10)

	def __str__(self):
		return self.gname

