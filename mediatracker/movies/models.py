from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    genre_name=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.genre_name

class Movie(models.Model):
    movie_title=models.CharField(max_length=255)
    release_date=models.DateField()
    language=models.CharField(max_length=255)
    running_time=models.IntegerField()
    release_country=models.CharField(max_length=255)
    created_date=models.DateTimeField(default=timezone.now)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.movie_title


class Actor(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    gender=models.CharField(max_length=1)

    def __str__(self) -> str:
        return self.first_name+" "+self.last_name


class MovieCast(models.Model):
    actor=models.ForeignKey(Actor,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    role=models.CharField(max_length=255)

class Review(models.Model):
    movie=models.ManyToManyField(Movie)
    reviewer=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    review_stars=models.IntegerField()
    review_text=models.TextField()
    





