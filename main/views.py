from django.shortcuts import *
from django.http import *
from pics.models import *

# Create your views here.

def main(request):
    p = Pic.objects.all()
    data = {'p': p[0]}
    res = render(request, 'main.html', context=data)
    return res
