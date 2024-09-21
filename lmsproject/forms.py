from  django import forms
from django.forms.widgets import PasswordInput
class Signin(forms.Form):
    username=forms.CharField(max_length=50)
    email=forms.EmailField()
    password=forms.CharField(widget=PasswordInput)
    repeatpassword=forms.CharField(widget=PasswordInput)