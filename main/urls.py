from django.urls import *
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
]