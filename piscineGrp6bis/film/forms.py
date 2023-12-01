from django import forms
from .models import Movie, Director

class MovieForm(forms.Form):
    title = forms.CharField(max_length=90, error_messages={'required': 'Le titre est obligatoire.'})
    director = forms.CharField(max_length=90, error_messages={'required': 'Le directeur est obligatoire.'})
    summary = forms.Textarea()
    duration = forms.DateField()
    date = forms.DateField()

class DirectorForm(forms.Form):
    name = forms.CharField(max_length=90, error_messages={'required': 'Le prénom est obligatoire.'})
    surname = forms.CharField(max_length=90, error_messages={'required': 'Le nom est obligatoire.'})
    resume = forms.Textarea()