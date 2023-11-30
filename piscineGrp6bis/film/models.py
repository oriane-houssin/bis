from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=90)
    realisator = models.CharField(max_length=90)
    realisator = models.ForeignKey('Realisator', on_delete=models.CASCADE, null=True, blank=True)
    realisator_bis = models.ManyToManyField('Realisator', related_name='posts', blank=True)
    summary = models.TextField(null=True)
    duration = models.DurationField
    date = models.DateField(null=False)

    def _str_(self):
        return self.title
    
class Realisator(models.Model):
    name = models.CharField(max_length=90)
    surname = models.CharField(max_length=90)
    resume = models.TextField(null=True)

    def _str_(self):
        return self.name
# Create your models here.
