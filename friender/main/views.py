from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.views import View


def information(request):
    return HttpResponse(f"<h1>Information</h1>")


def rules(request):
    return HttpResponse(f"<h1>Rules</h1>")

