from django.contrib import admin
from .models import Genre,Movie,Actor,MovieCast,Review
# Register your models here.

admin.site.register(Movie)
admin.site.register(MovieCast)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Review)