from django.db import models

# Create your models here.
class Batch(models.Model):
	name = models.CharField(max_length=256)

	def __str__(self):
		return self.name

class Image(models.Model):
	image = models.CharField(max_length=256)
	batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

	def __str__(self):
		return self.image