# Plik do definiowania widoków, które są renderowane za pomocą szablonizatora Jinja oraz wyświetlane w przeglądarce

from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie



# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def books(request):
    values = {
        'books': [
            {
                'title': 'The Hobbit, or There and Back Again',
                'author': 'J. R. R. Tolkien',
                'genre': 'High fantasy',   
                'year': 1937,
                'review': 'WIP',
            },
            {
                'title': 'The Lord of the Rings: The Fellowship of the Ring',
                'author': 'J. R. R. Tolkien',
                'genre': 'High fantasy',   
                'year': 1954,
                'review': 'WIP',
            },
            {
                'title': 'The Lord of the Rings: The Two Towers',
                'author': 'J. R. R. Tolkien',
                'genre': 'High fantasy',   
                'year': 1954,
                'review': 'WIP',
            },
            {
                'title': 'The Lord of the Rings: The Return of the King',
                'author': 'J. R. R. Tolkien',
                'genre': 'High fantasy',   
                'year': 1955,
                'review': 'WIP',
            }
        ]
    }

    return render(request, 'main/books.html', values)



# def movies(request):
#     values = {
#         'movies': [
            
#         ]
#     }

#     return render(request, 'main/movies.html', values)



def movies(request):
    # Dodaj tylko jeśli baza jest pusta (inicjalne dane)
    if Movie.objects.count() == 0:
        Movie.objects.bulk_create([
            Movie(title="The Lord of the Rings: The Fellowship of the Ring", description="Fantasy adventure in Middle-earth.", release_year=2001, genre="Fantasy"),
            Movie(title="The Shawshank Redemption", description="Prison escape drama based on a Stephen King novella.", release_year=1994, genre="Drama"),
            Movie(title="Star Wars: A New Hope", description="The original epic space opera.", release_year=1977, genre="Sci-Fi"),
            Movie(title="The Hobbit: An Unexpected Journey", description="A hobbit sets out on an epic quest.", release_year=2012, genre="Fantasy"),
            Movie(title="John Wick", description="A retired hitman seeks revenge.", release_year=2014, genre="Action"),
            Movie(title="The Matrix", description="A hacker discovers reality is a simulation.", release_year=1999, genre="Sci-Fi"),
            Movie(title="Pulp Fiction", description="Stylized crime stories intertwine in LA.", release_year=1994, genre="Crime"),
            Movie(title="Titanic", description="Tragic romance aboard a doomed ship.", release_year=1997, genre="Romance"),
            Movie(title="Forrest Gump", description="A simple man’s life story in historical events.", release_year=1994, genre="Drama"),
            Movie(title="The Dark Knight", description="Batman faces the Joker in a gritty Gotham.", release_year=2008, genre="Action")
        ])

    movies = Movie.objects.all()
    return render(request, 'main/movies.html', {'movies': movies})



def about(request):
    return render(request, 'main/about.html')



def aboutproject(request):
    return render(request, 'main/aboutproject.html')