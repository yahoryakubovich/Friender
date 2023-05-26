from django.contrib import admin
from django.urls import path, include
from .views import EstablishmentsApiView
from django.views.generic import *

urlpatterns = [
    path('establishments/', EstablishmentsApiView.as_view())
]