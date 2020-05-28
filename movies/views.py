from django.shortcuts import render
import tmdbsimple as tmdb
from decouple import config
from googleapiclient.discovery import build


# Create your views here.
tmdb.API_KEY=config('API_KEY')
API_KEY=config('DEVELOPER_KEY')


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
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    movie_name = movie['original_title']
    req = youtube.search().list(q=movie_name, part='snippet', type='video', maxResults=1)
    res = req.execute()
    for result in res.get('items'):
        if result['id']['kind'] == 'youtube#video':
            video_id = result['id']['videoId']
    return render(request, 'single_movie.html', {'movie':movie, 'videoId':video_id})

def single_show(request, tv_id):
    """
    view function renders template that displays the details of a single TV show
    """
    show = tmdb.TV(tv_id)
    show = show.info()
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    show_name = show['original_name']
    req = youtube.search().list(q=show_name, part="snippet", type='video', maxResults=1)
    res = req.execute()
    for result in res.get('items'):
        if result['id']['kind'] == 'youtube#video':
            video_id = result['id']['videoId']
    return render(request, 'single_show.html', {"show":show, 'videoId':video_id})
