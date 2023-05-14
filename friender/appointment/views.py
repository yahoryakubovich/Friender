from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import *


def all_friends(request):
    context = {
        "friends": Users.objects.all(),
    }
    return render(request, "friends.html", context=context)


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


def establishment_rating(request):
    context = {
        "ratings": EstablishmentsRating.objects.all().select_related('establishment')
    }
    return render(request, "establishment_rating.html", context=context)


def user_form_rating(request, **kwargs):
    user_id = int(kwargs['id'])
    context = {}
    if request.method == "POST":
        form = UserFormRating(request.POST)
        context["form"] = form
        if form.is_valid():
            UserRating.objects.create(
                user_id=user_id,
                rating=request.POST['rating'],
                description=request.POST['description'],
            )
            return HttpResponseRedirect("/appointment/user_rating")
    else:
        form = UserFormRating()
        context["form"] = form
    return render(request, "user_form_rating.html", context=context)


def establishment_form_rating(request, **kwargs):
    establishment_id = int(kwargs['id'])
    context = {}
    if request.method == "POST":
        form = EstablishmentFormRating(request.POST)
        context["form"] = form
        if form.is_valid():
            EstablishmentsRating.objects.create(
                establishment_id=establishment_id,
                rating=request.POST['rating'],
                description=request.POST['description'],
            )
            return HttpResponseRedirect("/appointment/establishment_rating")
    else:
        form = EstablishmentFormRating()
        context["form"] = form
    return render(request, "establishments_form_rating.html", context=context)


def create_user_form(request):
    context = {}
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        context["form"] = form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/appointment/friends")
    else:
        form = CreateUserForm()
        context["form"] = form
    return render(request, "create_user_form.html", context=context)


def create_appointment_form(request):
    context = {}
    if request.method == "POST":
        form = CreateAppointmentForm(request.POST)
        context["form"] = form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/appointment/friends")
    else:
        form = CreateAppointmentForm()
        context["form"] = form
    return render(request, "create_appointment_form.html", context=context)
