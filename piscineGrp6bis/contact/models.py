from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()

    def _str_(self):
        return f"Merci pour votre retour {self.name}!"