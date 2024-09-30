from django.db import models

# Create your models here.
class Programer(models.Model):
    username = models.CharField(max_length=120)
    bio = models.TextField(max_length=250,null=True,blank=True)
    
    