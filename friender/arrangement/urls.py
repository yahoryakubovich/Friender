from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('time_now/', current_datetime),
    path('greeting/<str:name>/', greeting),
    path('class_view/', Example.as_view()),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', year_archive)
]