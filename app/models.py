from django.db import models

# Create your models here.
from django import forms
from django.contrib.auth.models import User


class Registration(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    profile_pic=models.ImageField()
    