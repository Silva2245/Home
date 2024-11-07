from django import forms
from django.forms import *


class sufrm(forms.Form):
    uname = CharField(widget=TextInput(attrs={'class':'form-control', 
                                              'id':"floatingInput", 
                                              'placeholder': "name@example.com",
                                              'type': 'text'}), 
                      max_length=55, required=False)
    passwd = CharField(widget=PasswordInput(attrs={'class':'form-control', 
                                                   'id':"floatingPassword", 
                                                   'placeholder': "name@example.com", 
                                                   'type': 'password'}), 
                       max_length=55, required=False)
    
class sifrm(forms.Form):
    uname = CharField(widget=TextInput(attrs={'class':'form-control', 
                                              'id':"floatingInput", 
                                              'placeholder': "name@example.com",
                                              'type': 'text'}), 
                      max_length=55, required=False)
    passwd = CharField(widget=PasswordInput(attrs={'class':'form-control', 
                                                   'id':"floatingPassword", 
                                                   'placeholder': "name@example.com", 
                                                   'type': 'password'}), 
                       max_length=55, required=False)
    rm = BooleanField(widget=CheckboxInput(attrs={'type':"checkbox", 'value':"remember-me"}))