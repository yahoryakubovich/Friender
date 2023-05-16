from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import *
from .models import *

SEX = [
    ("M", "Male"),
    ("F", "Female")
]


class UserFormRating(forms.ModelForm):
    class Meta:
        model = UserRating
        fields = ["rating", "description"]
        widgets = {
            "description": forms.Textarea(attrs={'class': 'form-input'}),
        }


class EstablishmentFormRating(forms.ModelForm):
    class Meta:
        model = EstablishmentsRating
        fields = ["rating", "description"]
        widgets = {
            "description": forms.Textarea(attrs={'class': 'form-input'}),
        }


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ('email',)


class CreateAppointmentForm(forms.Form):
    host = forms.ChoiceField(choices=Host.objects.values_list('id', 'name'))
    place = forms.ChoiceField(choices=Establishments.objects.values_list('id', 'name'))
