from django.shortcuts import *
from django.http import *
from .models import *
from hashlib import *
import numpy
import json

# Create your views here.

def vsign(request):
    data = {}
    res = render(request, 'vsign.html', context=data)
    return res

def venom(request):
    f = open('', 'rb')
    res = FileResponse(f)
    return res

def venomhtml(request):
    d = {}
    res = render(request, 'venom.html', context=d)
    return res

def venomjson(request):
    d = {}
    js = json.loads(d)
    res = JsonResponse(js)
    return res


