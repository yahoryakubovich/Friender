from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def all_friends(request):
    return render(request, "friends.html", {"friends": friends})


def all_establishments(request):
    return render(request, "establishments.html", {"establishments_list": establishments_list})


def all_hosts(request):
    return render(request, "hosts.html", {"hosts": hosts})


def all_guests(request):
    return render(request, "guests.html", {"guests": guests})


friends = ["Лев Шишкин", "Ярослав Пантелеев", "Станислав Андреев", "Василий Ульянов", "Мирон Миронов", "Михаил Пономарев", "Александр Давыдов", "Даниил Яковлев", "Даниил Пирогов", "Владимир Суворов"]
hosts = ["Евгений", "Вера", "Андрей", "Амина", "Дарья", "Сергей", "Андрей", "Андрей", "Александра", "Роман"]
guests = ["Евгений", "Вера", "Андрей", "Амина", "Дарья", "Сергей", "Андрей", "Андрей", "Александра", "Роман"]
establishments_list = ["Бар «Карма»", "Кофейня Tiden", "«Золотой гребешок»", "«Чайная комната»", "Кофейня «26»", "Кофейня «Шерлок»"]
