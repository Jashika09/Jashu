from django import forms
from app1.models import Register, Login, Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    name=forms.CharField(max_length=200)
    lastname=forms.CharField(max_length=200)
    emailid=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200)


    class Meta:
        model=Register
        fields=('name','lastname','emailid','password',)


class LoginForm(forms.ModelForm):
    emailid=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200)


    class Meta:
        model=Login
        fields=('emailid','password',)


class ContactForm(forms.ModelForm):
    name=forms.CharField(max_length=200)
    lastname=forms.CharField(max_length=200)
    emailid=forms.CharField(max_length=200)
    feedback=forms.CharField(max_length=200)


    class Meta:
        model=Contact
        fields=('name','lastname','emailid','feedback',)


class SignForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')
