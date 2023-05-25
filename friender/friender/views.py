from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView,TemplateResponseMixin, ContextMixin



def home(request):
    return render(request, "home.html")
