from django import forms


class RatingUserForm(forms.Form):
    rating = forms.IntegerField()
    description = forms.CharField()
