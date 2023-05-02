from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('establishments/', all_establishments, name='establishments'),
    path('hosts/', all_hosts, name='hosts'),
    path('guests/', all_guests, name='guests'),
    re_path(r"^rating_user/((?P<id>[0-9]+)/)?$", user_form_rating, name = "user_form_rating")
]
