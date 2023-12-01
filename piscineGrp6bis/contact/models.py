from django.db import models

class Question(models.Model):
    nom = models.CharField(max_length=20)
    adresse_email = models.EmailField(max_length=20)
    message = models.TextField(null=True)
    def str(self):
        return self.nom
