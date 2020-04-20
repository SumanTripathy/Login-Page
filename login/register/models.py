from django.db import models

# Create your models here.

class data(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
