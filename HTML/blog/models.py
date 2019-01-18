from django.db import models

# Create your models here.
class Post(models.Model):
	prag =models.IntegerField(default=0)
	plas = models.IntegerField(default=0)
	bldprs = models.IntegerField(default=0)
	skin = models.IntegerField(default=0)
	serum = models.IntegerField(default=0)
	BMI = models.IntegerField(default=0)
	pedigree = models.IntegerField(default=0)
	age = models.IntegerField(default=0)

