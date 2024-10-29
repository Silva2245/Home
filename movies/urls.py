from django.urls import *
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movieshome, name='movieshome'),
    path('movie/', views.movie, name='movie')
]