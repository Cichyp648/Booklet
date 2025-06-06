from django.shortcuts import render
from movies.models import Movie
from books.models import Book  # ✅ correct import based on your app structure
import random

def index(request):
    movies = Movie.objects.all()
    books = Book.objects.all()

    movie = random.choice(movies) if movies.exists() else None
    book = random.choice(books) if books.exists() else None

    return render(request, 'main/index.html', {
        'random_movie': movie,
        'random_book': book
    })

def about(request):
    return render(request, 'main/about.html')


def aboutproject(request):
    return render(request, 'main/aboutproject.html')

def contact(request):
    return render(request, 'main/contact.html')

def forum_home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'forum/forum_home.html', {'posts': posts})