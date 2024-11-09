from django.shortcuts import *
from django.http import *
from pics.models import *
import base64

# Create your views here.

def main(request):
    p = Pic.objects.all()
    data = {'p': p[0]}
    res = render(request, 'main.html', context=data)
    return res

def homee(request):
    data = {}
    res = render(request, 'home.html', context=data)
    return res

def about(request):
    data = {}
    res = render(request, 'about.html', context=data)
    return res

def profile(request):
    uv = request.COOKIES['uv']
    print(uv)
    um = base64.b64decode()
    print(um) 
    data = {}
    res = render(request, 'profile.html', context=data)
    return res
