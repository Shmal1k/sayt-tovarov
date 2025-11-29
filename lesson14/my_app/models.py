from django.db import models

# Create your models here.

class Tovar(models.Model):
    name = models.CharField(max_length=100) #будет создано поле name типа varchar(100)
    price = models.IntegerField()
    info = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    opisanie = models.CharField(max_length=100)