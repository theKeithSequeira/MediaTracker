from django.shortcuts import render

# Create your views here.
def movie_list(request):
    return render(request,'movies/movie_list.html',{})