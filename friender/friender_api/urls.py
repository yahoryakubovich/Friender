from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.generic import *

urlpatterns = [
    path('establishments/', EstablishmentsListAPIView.as_view()),
    path('establishments/<int:pk>', EstablishmentsListAPIViewDetail.as_view())
]
