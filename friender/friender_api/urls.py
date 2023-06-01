from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.generic import *

urlpatterns = [
    path('establishments/', EstablishmentsListAPIView.as_view()),
    path('establishments/<int:pk>', EstablishmentsListAPIViewDetail.as_view()),
    path('hobbies/', HobbiesListAPIView.as_view()),
    path('hobbies/<int:pk>', HobbiesListAPIViewDetail.as_view()),
    path('hobbies/<str:name_hobby>', UsersApiView.as_view())
]
