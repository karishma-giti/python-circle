from django.db import models

# Create your models here.
class UserSkills(models.Model):
    username = models.CharField(max_length=25,unique=True)  
    name = models.CharField(max_length=100,null=False,default=False)  
    skill = models.CharField(max_length=250,null=False,default=False)
   


