from django.db import models

# Create your models here.
class Image(models.Model):
	name = models.CharField(max_length=256)

	def __str__(self):
		return self.name