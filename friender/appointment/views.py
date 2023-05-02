from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *


def all_establishments(request):
    context = {
        "establishments": Establishments.objects.all(),
    }
    return render(request, "establishments.html", context=context)


def all_hosts(request):
    context = {
        "hosts": Host.objects.all(),
    }
    return render(request, "hosts.html", context=context)


def all_guests(request):
    context = {
        "guests": Guest.objects.all(),
    }
    return render(request, "guests.html", context=context)


def user_form_rating(request, **kwargs):
    user_id = int(kwargs['id'])
    context = {
        "user": Users.objects.get(id=user_id)
    }
    return render(request, "userrating.html", context=context)
