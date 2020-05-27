from django.shortcuts import render
import tmdbsimple as tmdb
import os
from decouple import config

# Create your views here.
tmdb.API_KEY=config('API_KEY')
print(tmdb.API_KEY)

def index(request):
    """
    view function returns template that displays popular and upcoming movies
    """
    popular_movies_tmdb = tmdb.Movies('popular')
    popular_movies = popular_movies_tmdb.info()['results']

    upcoming_movies_tmdb = tmdb.Movies('upcoming')
    upcoming_movies = upcoming_movies_tmdb.info()['results']

    return render(request, 'movies.html', {"popular":popular_movies, 'upcoming':upcoming_movies})