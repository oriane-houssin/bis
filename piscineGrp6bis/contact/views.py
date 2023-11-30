from django.shortcuts import render
from django.http import HttpResponse

def question(request):
    return HttpResponse("Question")
