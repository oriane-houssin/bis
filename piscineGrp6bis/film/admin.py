from django.contrib import admin
from .models import Director, Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'duration', 'date')
    list_filter = ('director', 'date')
    search_fields = ('title', 'director')

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    search_fields = ('name', 'surname')

# Register your models here.
