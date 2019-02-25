from django.urls import path
from . import views

# ROUTING TO CERTIAN FUNCTIONS
urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/movieDetails/<int:movie_id>/', views.movieDetails, name='movieDetails'),
    path('home/movieSynopsis/<int:movie_id>/', views.movieSynopsis, name='movieSynopsis'),

]