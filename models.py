from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
class Book(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    author=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)

class BRMuser(models.Model):
    #user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=20,)
    username=models.CharField(max_length=20,unique=True,null=True)
    password=models.CharField(max_length=20,null=True)
    phone=PhoneNumberField(unique=True)
    def __str__(self):
        return self.username
