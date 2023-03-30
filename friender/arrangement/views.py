from django.shortcuts import render

from django.http import HttpResponse
import datetime
from django.views import View


def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is {now} now.</body></html>"
    return HttpResponse(html)


def greeting(request, name):
    return HttpResponse(f"<h1>Hello {name}</h1>")


def year_archive(request, year):
    return HttpResponse(f"<h1>{year}</h1>")


class Example(View):
    def get(self, request):
        return HttpResponse(f"<h1>This is class base view</h1>")
