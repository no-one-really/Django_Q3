from django.db import models

# Create your models here.
class slots(models.Model):
    """docstring for Exam."""


    slot = models.IntegerField()
    name = models.CharField(max_length=100)

class point1(models.Model):
    x=models.IntegerField()
    y=models.IntegerField()

class itemsinput(models.Model):
    inputitem= models.CharField(max_length=100)
