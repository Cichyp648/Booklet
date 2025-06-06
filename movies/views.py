from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm, MovieReviewForm

def index(request):
    movies = Movie.objects.all()

    if request.method == 'POST':
        if 'rating' in request.POST:
            # Review submitted
            movie_id = request.POST.get('movie_id')
            movie = get_object_or_404(Movie, pk=movie_id)
            review_form = MovieReviewForm(request.POST)
            if review_form.is_valid():
                rating = review_form.cleaned_data['rating']
                movie.review_count += 1
                movie.review_sum += rating
                movie.save()
                return redirect('movie_index')
        else:
            # New movie submitted
            form = MovieForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('movie_index')
    else:
        form = MovieForm()

    review_form = MovieReviewForm()
    return render(request, 'movies/index.html', {
        'form': form,
        'review_form': review_form,
        'movies': movies
    })
