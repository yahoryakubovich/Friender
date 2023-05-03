from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import *


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


def user_rating(request):
    context = {
        "ratings": UserRating.objects.all().select_related('user')
    }
    return render(request, "user_rating.html", context=context)


def user_form_rating(request, **kwargs):
    user_id = int(kwargs['id'])
    if request.method == "POST":
        form = RatingUserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            UserRating.objects.create(
                user_id = user_id,
                rating=request.POST['rating'],
                description=request.POST['description'],
            )
            return HttpResponseRedirect("/appointment/user_rating")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RatingUserForm()

    return render(request, "user_form_rating.html", {"form": form})
