from django.contrib.auth.models import AbstractUser
from django.db import models

class UtilisateurPersonnalise(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(null=False)
    # Ajoutez d'autres champs personnalisés au besoin

    def __str__(self):
        return self.email
