from django import forms
from django.shortcuts import render, redirect

class Question(forms.Form):
    nom = forms.CharField(max_length=200)
    adresse_email = forms.EmailField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)

def contact(request):
    if request.method == 'POST':
        form = Question(request.POST)
        if form.is_valid():
            
            nom = form.cleaned_data['nom']
            adresse_email = form.cleaned_data['adresse_email']
            message = form.cleaned_data['message']


            return redirect('home')
    else:
        form = Question()

    return render(request, 'contact.html', {'form': form})
