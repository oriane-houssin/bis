from django.urls import path
from .views import form_movie, list_movies, detail_movie, form_director, detail_director, list_directors

urlpatterns = [
    path('', list_movies),
    path('directors/', list_directors, name='directors'),
    path('detail-movie/<int:id>/', detail_movie, name='detail'),
    path('detail-director/<int:id>/', detail_director, name='detail'),
    path('form-movie/', form_movie, name='form'),
    path('form-director/', form_director, name='form'),
]