# Plik do definiowania widoków, które są renderowane za pomocą szablonizatora Jinja oraz wyświetlane w przeglądarce

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def cars(request):
    values = {
        'cars': [
            {
                'car': 'The Hobbit, or There and Back Again',
                'author': 'J. R. R. Tolkien',
                'genre': 'Fantasy',   
                'year': 1937,
                'review': 'WIP',
            }
        ]
    }

    return render(request, 'main/cars.html', values)

def about(request):
    return render(request, 'main/about.html')