from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('friends/', all_friends, name='friends'),
    path('establishments/', all_establishments, name='establishments'),
    path('hosts/', all_hosts, name='hosts'),
    path('guests/', all_guests, name='guests'),
    path('user_rating/', user_rating, name='user_rating'),
    path('establishment_rating/', establishment_rating, name='establishment_rating'),
    re_path(r"^user_rating/(?P<id>[\d-]+)$", user_form_rating, name="user_form_rating"),
    re_path(r"^establishment_rating/(?P<id>[\d-]+)$", establishment_form_rating, name="establishment_form_rating"),
    path('create_user/', create_user_form, name='create_user'),
    path('create_appointment/', create_appointment_form, name='create_appointment'),
]
