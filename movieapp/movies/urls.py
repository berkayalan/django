from django.urls import path
from . import views

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/home
# http://127.0.0.1:8000/movies
# http://127.0.0.1:8000/movies/3
# http://127.0.0.1:8000/movies/titanic

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("movies", views.movies, name="movies"),
    path("categories", views.categories, name="categories"),
    path("categories/<str:category_name>", views.category_details, name="category_details"),
    path("movies/<int:id>", views.movie_details, name="details"),
    path("movies/<str:category_name>", views.category_filter, name="category_filter")
]