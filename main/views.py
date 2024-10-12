from django.shortcuts import *
from django.http import *

# Create your views here.

def main(request):
    data = {}
    res = render(request, 'main.html', context=data)
    return res
