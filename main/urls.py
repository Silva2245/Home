from django.urls import *
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', views.homee, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile')
]