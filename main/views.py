# Plik do definiowania widoków, które są renderowane za pomocą szablonizatora Jinja oraz wyświetlane w przeglądarce

from django.shortcuts import render

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



def movies(request):
    values = {
        'movies': [
            
        ]
    }

    return render(request, 'main/movies.html', values)



def about(request):
    return render(request, 'main/about.html')



def aboutproject(request):
    return render(request, 'main/aboutproject.html')