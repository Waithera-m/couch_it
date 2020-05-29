from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>', views.single_movie, name="single_movie"),
    path('show/<int:tv_id>', views.single_show, name="single_show"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    