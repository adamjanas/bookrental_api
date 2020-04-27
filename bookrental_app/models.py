from django.db import models

class Kind(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):

		return self.name




class Book(models.Model):
	name = models.CharField(max_length=50)
	kind = models.ForeignKey(Kind, on_delete=models.CASCADE)

	def __str__(self):

		return self.name



class Reader(models.Model):
	name = models.CharField(max_length=50)
	books = models.ManyToManyField(Book)

	def __str__():

		return self.name
