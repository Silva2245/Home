from django.urls import *
from . import views

app_name = 'venom'

urlpatterns = [
    path('', views.vsign, name='vsign')
]