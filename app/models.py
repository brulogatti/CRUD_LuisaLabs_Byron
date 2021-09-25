from django.db import models
from django.urls import reverse

# Create your models here.
class Companies(models.Model):
    cmpId = models.PositiveBigIntegerField()
    cmpCnpj = models.CharField(max_length=16)
    cmpName = models.CharField(max_length=50)
    cmpPassword = models.CharField(max_length=20)
    cmpAddress = models.CharField(max_length=50)
    cmpEmail = models.CharField(max_length=20)
    cmpPhone = models.CharField(max_length=14)

class Products(models.Model):
    prodId = models.PositiveBigIntegerField()
    prodName = models.CharField(max_length=50)
    prodCompany = models.CharField(max_length=50)
    prodDescription = models.CharField(max_length=200)
    prodPrice = models.FloatField()






