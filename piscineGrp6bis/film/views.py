from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from film.models import Director, Movie
from film.forms import MovieForm, DirectorForm

def list_movies(request):
    title = "Movies"
    movies = Movie.objects.all().order_by('date')
    context = {
        'title' : title,
        'movies' : movies

    }
    return render(request, 'film/list-movies.html', context)

def list_directors(request):
    title = "Directors"
    directors = Director.objects.all().order_by('name')
    context = {
        'directors' : directors,
        'title' : title

    }
    return render(request, 'film/list-directors.html', context)

def detail_movie(request, id):
    print(request.GET)

    movie = get_object_or_404(Movie, pk=id)
    context = {
        'title' : movie.title,
        'director' : movie.director,
        'summary' : movie.summary,
        'duration' : movie.duration,
        'date' : movie.date
    }
    return render(request, 'film/detail-movie.html', context)

def detail_director(request, id):
    print(request.GET)

    director = get_object_or_404(Director, pk=id)
    context = {
        'name' : director.name,
        'surname' : director.surname,
        'resume' : director.resume,
    }
    return render(request, 'film/detail-director.html', context)

def form_movie(request):
    print(request.POST)
    print(request.GET)
    form = MovieForm()

    if request.method == 'POST':
        form = MovieForm(request.POST)
    
        if form.is_valid():
            title = form.cleaned_data['title']
            director = form.cleaned_data['director']
            summary = form.cleaned_data['summary']
            duration = form.cleaned_data['duration']
            date = form.cleaned_data['date']
            print(form.cleaned_data)

            Movie.objects.create(**form.cleaned_data)

        else:
            print('The form is not valid please try again')

    else: 
        form = MovieForm()

    return render(request, 'film/form.html', {'formulaire': form})

def form_director(request):
    print(request.POST)
    print(request.GET)
    form = DirectorForm()

    if request.method == 'POST':
        form = DirectorForm(request.POST)
    
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            resume = form.cleaned_data['resume']
            print(form.cleaned_data)

            Director.objects.create(**form.cleaned_data)

        else:
            print('The form is not valid please try again')

    else: 
        form = DirectorForm()

    return render(request, 'film/form.html', {'formulaire': form})

