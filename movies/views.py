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

    popular_shows_tmdb = tmdb.TV('popular')
    popular_shows = popular_shows_tmdb.info()['results']

    current_shows_tmdb = tmdb.TV('airing_today')
    current_shows = current_shows_tmdb.info()['results']

    top_shows_tmdb = tmdb.TV('top_rated')
    top_shows = top_shows_tmdb.info()['results']

    return render(request, 'movies.html', {"popular":popular_movies, 'upcoming':upcoming_movies, 'shows':popular_shows, "current":current_shows, 'top':top_shows})

def single_movie(request, movie_id):
    """
    view function renders template that displays the details of a single movie
    """
    movie = tmdb.Movies(movie_id)
    movie = movie.info()
    return render(request, 'single_movie.html', {'movie':movie})
