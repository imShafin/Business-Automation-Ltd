from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    university = models.CharField(max_length=100)