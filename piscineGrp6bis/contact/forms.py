from django import forms

class Question(forms.Form):
    nom = forms.CharField(max_length=200)
    adresse_email = forms.EmailField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)