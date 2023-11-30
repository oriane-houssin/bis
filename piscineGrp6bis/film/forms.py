from django import forms
from .models import Movie, Realisator

class MovieForm(forms.Form):
    title = forms.CharField(max_length=90)
    realisator = forms.CharField(max_length=90)
    summary = forms.Textarea()
    duration = forms.DateField()
    date = forms.DateField()

class RealisatorForm(forms.Form):
    