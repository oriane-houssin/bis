from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=90)
    director = models.CharField(max_length=90)
    director = models.ForeignKey('Director', on_delete=models.CASCADE, null=True, blank=True)
    director_bis = models.ManyToManyField('Director', related_name='posts', blank=True)
    summary = models.TextField(null=True)
    duration = models.DurationField
    date = models.IntegerField(null=False)

    def _str_(self):
        return self.title
    
class Director(models.Model):
    name = models.CharField(max_length=90)
    surname = models.CharField(max_length=90)
    resume = models.TextField(null=True)

    def _str_(self):
        return self.name

