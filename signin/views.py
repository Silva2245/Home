from django.shortcuts import *
from django.http import *

# Create your views here.

def signinhome(request):
    data = {}
    res = render(request, 'signin.html', context=data)
    return res

def signup(request):
    data = {}
    res = render(request, 'signup.html', context=data)
    return res
