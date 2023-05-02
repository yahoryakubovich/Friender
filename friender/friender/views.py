from django.shortcuts import render


def friender(request):
    return render(request, "friender.html")


def home(request):
    return render(request, "home.html")

