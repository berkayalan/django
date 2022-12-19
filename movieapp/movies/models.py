from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.CharField(max_length=100)
    category_detail = models.TextField(max_length=500, default="This category will be defined soon!")

class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_year = models.CharField(max_length=4)
    movie_image = models.TextField(max_length=500)
    movie_link = models.TextField(max_length=500)
    movie_mainpage = models.BooleanField(default=False)
    movie_category = models.CharField(max_length=100, default="This category of this movie will be defined soon!")

# Create your models here.
