from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import *
from .models import *
from django.db import transaction
from django.core.paginator import Paginator


def all_friends(request):
    users = Users.objects.all().prefetch_related('hobbies_set', 'userrating_set')
    paginator = Paginator(users, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "friends": users,
        "page_obj": page_obj
    }
    return render(request, "friends.html", context=context)


def all_establishments(request):
    establishments = Establishments.objects.all()
    paginator = Paginator(establishments, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "establishments": establishments,
        "page_obj": page_obj
    }
    return render(request, "establishments.html", context=context)


def all_hosts(request):
    hosts = Host.objects.all()
    paginator = Paginator(hosts, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "hosts": hosts,
        "page_obj": page_obj
    }
    return render(request, "hosts.html", context=context)


def all_guests(request):
    guests = Guest.objects.all()
    paginator = Paginator(guests, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "guests": guests,
        "page_obj": page_obj
    }
    return render(request, "guests.html", context=context)


def user_rating(request):
    userratings = UserRating.objects.all().select_related('user')
    paginator = Paginator(userratings, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "userratings": userratings,
        "page_obj": page_obj
    }
    return render(request, "user_rating.html", context=context)


def establishment_rating(request):
    estratings = EstablishmentsRating.objects.all().select_related('establishment')
    paginator = Paginator(estratings, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "estratings": estratings,
        "page_obj": page_obj
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


@transaction.atomic
def create_appointment_form(request):
    context = {}
    if request.method == "POST":
        form = CreateAppointmentForm(request.POST)
        context["form"] = form
        guest = Guest.objects.all().order_by('?')[0]
        if form.is_valid():

            host_id = int(request.POST['host'][0])
            place_id = int(request.POST['place'][0])

            # host = Host.objects.get(id=host_id),
            # establishments = Establishments.objects.get(id=place_id)

            host = Host.objects.filter(users_ptr_id=host_id).select_for_update()[0]
            establishments = Establishments.objects.get(id=place_id)

            if host.status == 'A':
                host.status = 'B'
                host.save()
                Appointments.objects.create(
                    host=host,
                    guest=Guest.objects.get(id=guest.id),
                    establishments=establishments
                )
            else:
                raise ValueError("Пользователь уже занят")
            return HttpResponseRedirect("/appointment/friends")
    else:
        form = CreateAppointmentForm()
        context["form"] = form
    return render(request, "create_appointment_form.html", context=context)


@transaction.atomic
def make_an_order(request):
    context = {}
    if request.method == "POST":
        form = MakeAnOrder(request.POST)
        context["form"] = form
        if form.is_valid():
            appointment = (request.POST['appointment'][0])
            price = int(request.POST['price'])
            host = Host.objects.get(appointments=appointment)

            if host.max_spend_value >= price:
                host.max_spend_value = host.max_spend_value - price
                host.save()
                form.save()
            else:
                raise ValueError("Недостаточно средств")
            return HttpResponseRedirect("/appointment/friends")
    else:
        form = MakeAnOrder()
        context["form"] = form
    return render(request, "make_an_order.html", context=context)
