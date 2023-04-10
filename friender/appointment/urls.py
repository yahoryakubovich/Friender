from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('friends/', all_friends, name='friends'),
    path('establishments/', all_establishments, name='establishments'),
    path('hosts/', all_hosts, name='hosts'),
    path('guests/', all_guests, name='guests'),
    path('rating/', rating, name='rating')
]
