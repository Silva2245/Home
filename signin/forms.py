from django import forms
from django.forms import *


class sufrm(forms.Form):
    uname = CharField(widget=TextInput(attrs={}), max_length=55, required=False)
    passwd = CharField(widget=PasswordInput(attrs={}), max_length=55, required=False)