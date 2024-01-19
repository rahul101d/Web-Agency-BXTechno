from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
 
# Create your models here.


class standard(BaseModel):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    mobnumber=models.IntegerField()
    plan=models.CharField(max_length=30,default='Standard')
    message=models.CharField(max_length=500)

class ecommlite(BaseModel):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    mobnumber=models.IntegerField()
    plan=models.CharField(max_length=30,default='eCommlite')
    message=models.CharField(max_length=500)

class ecommpro(BaseModel):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    mobnumber=models.IntegerField()
    plan=models.CharField(max_length=30,default='ecommpro')
    message=models.CharField(max_length=500)