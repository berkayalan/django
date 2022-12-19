from django.shortcuts import render
from .models import Category,Movie

def home(request):
    data = {
        "categories" : Category.objects.all(),
        "movies": Movie.objects.all() #filter(movie_category = "Drama")
    }
    return render(request, "index.html",data)

def movies(request):

    data = {
        "categories" : Category.objects.all(),
        "movies": Movie.objects.all()
    }
    return render(request, "movies.html",data)

def categories(request):

    data = {
        "categories" : Category.objects.all()
    }
    return render(request, "categories.html",data)

def category_details(request, category_name):

    data = {
        "category" : Category.objects.get(category_name = category_name)
    }
    return render(request, "category_details.html",data)

def movie_details(request, id):

    data = {
        "movie": Movie.objects.get(id=id)
    }
    return render(request, "details.html", data)

def category_filter(request, category_name):
    data = {
        "movie": Movie.objects.filter(movie_category = category_name),
        "categories" : Category.objects.all()
    }
    return render(request, "category_filter.html", data)
