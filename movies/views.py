from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def index(request):
    movies = Movie.objects.all()

    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_index')  # Must match your URL name
    else:
        form = MovieForm()

    return render(request, 'movies/index.html', {'form': form, 'movies': movies})
