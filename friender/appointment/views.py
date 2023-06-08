from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import *
from .models import *
from django.db import transaction
from django.core.paginator import Paginator
from django.views.generic import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.cache import cache

from django.urls import reverse_lazy


class FriendListView(LoginRequiredMixin, ListView):
    login_url = "/admin/login"
    template_name = "friends.html"
    model = Users
    context_object_name = "users"
    paginate_by = 5
    cache.clear()


class EstablishmentListView(PermissionRequiredMixin, ListView):
    permission_required = "appointment.view_establishments"
    model = Establishments
    template_name = "establishments.html"
    context_object_name = "establishments"
    paginate_by = 5
    permission_denied_message = "Отказано в доступе"
    raise_exception = True

    def get_permission_denied_message(self):
        """
        Override this method to override the permission_denied_message attribute.
        """
        return self.permission_denied_message


class HostListView(ListView):
    template_name = "hosts.html"
    model = Host
    context_object_name = "hosts"
    paginate_by = 5
    cache.clear()


class GuestListView(ListView):
    template_name = "guests.html"
    model = Guest
    context_object_name = "guests"
    paginate_by = 5


class UserRatingListView(ListView):
    template_name = "user_rating.html"
    model = UserRating
    context_object_name = "ratings"
    paginate_by = 5


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


class EstablishmentRatingListView(ListView):
    template_name = "establishment_rating.html"
    model = EstablishmentsRating
    context_object_name = "ratings"
    paginate_by = 5


class UserCreateView(CreateView):
    template_name = "create_user_form.html"
    model = Users
    fields = ["name", "surname", "age", "sex", "email", "city", "photo"]
    success_url = "../friends"


def create_appointment_form(request):
    context = {}
    if request.method == "POST":
        form = CreateAppointmentForm(request.POST)
        context["form"] = form
        guest = Guest.objects.all().order_by('?')[0]
        if form.is_valid():
            host_id = int(request.POST['host'][0])
            place_id = int(request.POST['place'][0])

            establishments = Establishments.objects.get(id=place_id)
            hosts = Host.objects.select_for_update().filter(users_ptr_id=host_id)
            with transaction.atomic():
                for host in hosts:
                    if host.status == 'A' and host:
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


def make_an_order(request):
    context = {}
    if request.method == "POST":
        form = MakeAnOrder(request.POST)
        context["form"] = form
        if form.is_valid():
            appointment = (request.POST['appointment'][0])
            price = int(request.POST['price'])
            host = Host.objects.get(appointments=appointment)
            with transaction.atomic():
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
