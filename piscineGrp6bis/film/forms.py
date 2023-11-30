from django import forms
from .models import Movie, Director

class MovieForm(forms.Form):
    title = forms.CharField(max_length=90)
    director = forms.CharField(max_length=90)
    summary = forms.Textarea()
    duration = forms.DateField()
    date = forms.DateField()

class DirectorForm(forms.Form):
    name = forms.CharField(max_length=90)
    surname = forms.CharField(max_length=90)
    resume = forms.Textarea()