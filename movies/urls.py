from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>', views.single_movie, name="single_movie"),
    path('show/<int:tv_id>', views.single_show, name="single_show"),
]