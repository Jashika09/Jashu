from django.db import models

# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    emailid=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self):
        return name


class Login(models.Model):
    emailid=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self):
        return emailid


class Contact(models.Model):
    name=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    emailid=models.CharField(max_length=200)
    feedback=models.CharField(max_length=200)

    def __str__(self):
        return name
    
