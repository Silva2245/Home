from django.urls import *
from . import views

app_name = 'signin'

urlpatterns = [
    path('', views.signinhome, name='signinhome'),
    path('signup/', views.signup, name='signup')
]