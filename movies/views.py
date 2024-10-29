from django.shortcuts import *
from django.http import *
from .models import *

# Create your views here.

def movieshome(request):
    data = {}
    res = render(request, 'movies.html', context=data)
    return res

def movie(request):
    data = {}
    res = render(request, 'movie.html', context=data)
    return res
