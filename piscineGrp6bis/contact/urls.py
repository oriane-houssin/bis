from django.urls import path
from .views import question

urlpatterns = [
    path('detail/<int:id>/', question, name='question'),
]