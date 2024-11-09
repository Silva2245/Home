from django.shortcuts import *
from django.http import *
from .forms import *
from .models import *
from hashlib import *
import base64

# Create your views here.

def signinhome(request):
    frm = sifrm(request.POST)
    mem = Member.objects
    if frm.is_valid() == True and request.method == 'POST':
        unamee = frm.cleaned_data['uname']
        passwdd = frm.cleaned_data['passwd']
        sha = sha256(passwdd.encode('ascii'))
        pv = str(sha.hexdigest())
        memb = mem.get(uname=unamee)
        p = memb.passwd
        if p == pv:
            us = md5(unamee.encode('ascii'))
            uv = base64.b64encode(unamee.encode('ascii'))
            r = redirect('main:profile')
            r.set_cookie('uv', uv)
            r.set_cookie('pv', pv)
            return r
    data = {'frm': frm}
    res = render(request, 'signin.html', context=data)
    return res

def signup(request):
    frm = sufrm(request.POST)
    mem = Member.objects
    if frm.is_valid() == True and request.method == 'POST':
        unamee = frm.cleaned_data['uname']
        passwdd = frm.cleaned_data['passwd']
        sha = sha256(passwdd.encode('ascii'))
        pv = str(sha.hexdigest())
        mem.create(uname=unamee, passwd=pv)
        print('Member Added')
    data = {'frm': frm}
    res = render(request, 'signup.html', context=data)
    return res
