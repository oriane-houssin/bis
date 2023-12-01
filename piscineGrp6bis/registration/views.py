from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            utilisateur = form.save()
            login(request, utilisateur)  # Connecte automatiquement l'utilisateur après l'inscription
            return redirect('film')  # Redirige vers la page d'accueil après l'inscription
    else:
        form = CustomUserCreationForm()
    return render(request, 'login.html', {'form': form})
