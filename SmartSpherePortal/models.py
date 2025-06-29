from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=50),
    email = models.CharField(max_length=80),
    date = models.DateField(),
    password = models.CharField(max_length=8,nullable=false)
    
