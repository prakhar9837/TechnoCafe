from django.db import models
#from django.db import forms

# Create your models here.

class customerclass(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=32) 