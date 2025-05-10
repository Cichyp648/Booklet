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
            },
            {
                'title': 'The Silmarillion',
                'author': 'J. R. R. Tolkien',
                'genre': 'Mythopoeia',
                'year': 1977,
                'review': 'WIP',
            },
            {
                'title': 'A Game of Thrones',
                'author': 'George R. R. Martin',
                'genre': 'Epic fantasy',
                'year': 1996,
                'review': 'WIP',
            },
            {
                'title': 'A Clash of Kings',
                'author': 'George R. R. Martin',
                'genre': 'Epic fantasy',
                'year': 1998,
                'review': 'WIP',
            },
            {
                'title': 'A Storm of Swords',
                'author': 'George R. R. Martin',
                'genre': 'Epic fantasy',
                'year': 2000,
                'review': 'WIP',
            },
            {
                'title': 'Harry Potter and the Philosopher\'s Stone',
                'author': 'J. K. Rowling',
                'genre': 'Fantasy',
                'year': 1997,
                'review': 'WIP',
            },
            {
                'title': 'Harry Potter and the Chamber of Secrets',
                'author': 'J. K. Rowling',
                'genre': 'Fantasy',
                'year': 1998,
                'review': 'WIP',
            },
            {
                'title': 'Harry Potter and the Prisoner of Azkaban',
                'author': 'J. K. Rowling',
                'genre': 'Fantasy',
                'year': 1999,
                'review': 'WIP',
            },
            {
                'title': 'Dune',
                'author': 'Frank Herbert',
                'genre': 'Science Fiction',
                'year': 1965,
                'review': 'WIP',
            },
            {
                'title': 'Dune Messiah',
                'author': 'Frank Herbert',
                'genre': 'Science Fiction',
                'year': 1969,
                'review': 'WIP',
            },
            {
                'title': 'Foundation',
                'author': 'Isaac Asimov',
                'genre': 'Science Fiction',
                'year': 1951,
                'review': 'WIP',
            },
            {
                'title': 'Foundation and Empire',
                'author': 'Isaac Asimov',
                'genre': 'Science Fiction',
                'year': 1952,
                'review': 'WIP',
            },
            {
                'title': 'Second Foundation',
                'author': 'Isaac Asimov',
                'genre': 'Science Fiction',
                'year': 1953,
                'review': 'WIP',
            },
            {
                'title': 'The Name of the Wind',
                'author': 'Patrick Rothfuss',
                'genre': 'Fantasy',
                'year': 2007,
                'review': 'WIP',
            },
            {
                'title': 'The Wise Man\'s Fear',
                'author': 'Patrick Rothfuss',
                'genre': 'Fantasy',
                'year': 2011,
                'review': 'WIP',
            },
            {
                'title': 'Mistborn: The Final Empire',
                'author': 'Brandon Sanderson',
                'genre': 'Fantasy',
                'year': 2006,
                'review': 'WIP',
            },
            {
                'title': 'Mistborn: The Well of Ascension',
                'author': 'Brandon Sanderson',
                'genre': 'Fantasy',
                'year': 2007,
                'review': 'WIP',
            },
            {
                'title': 'Mistborn: The Hero of Ages',
                'author': 'Brandon Sanderson',
                'genre': 'Fantasy',
                'year': 2008,
                'review': 'WIP',
            },
            {
                'title': 'The Way of Kings',
                'author': 'Brandon Sanderson',
                'genre': 'Epic Fantasy',
                'year': 2010,
                'review': 'WIP',
            },
            {
                'title': 'Words of Radiance',
                'author': 'Brandon Sanderson',
                'genre': 'Epic Fantasy',
                'year': 2014,
                'review': 'WIP',
            },
            {
                'title': 'Warbreaker',
                'author': 'Brandon Sanderson',
                'genre': 'Fantasy',
                'year': 2009,
                'review': 'WIP',
            },
            {
                'title': 'The Lion, the Witch and the Wardrobe',
                'author': 'C. S. Lewis',
                'genre': 'Fantasy',
                'year': 1950,
                'review': 'WIP',
            },
            {
                'title': 'Prince Caspian',
                'author': 'C. S. Lewis',
                'genre': 'Fantasy',
                'year': 1951,
                'review': 'WIP',
            },
            {
                'title': 'The Voyage of the Dawn Treader',
                'author': 'C. S. Lewis',
                'genre': 'Fantasy',
                'year': 1952,
                'review': 'WIP',
            },
            {
                'title': 'The Catcher in the Rye',
                'author': 'J. D. Salinger',
                'genre': 'Literary Fiction',
                'year': 1951,
                'review': 'WIP',
            },
            {
                'title': '1984',
                'author': 'George Orwell',
                'genre': 'Dystopian',
                'year': 1949,
                'review': 'WIP',
            },
            {
                'title': 'Animal Farm',
                'author': 'George Orwell',
                'genre': 'Political satire',
                'year': 1945,
                'review': 'WIP',
            },
            {
                'title': 'Brave New World',
                'author': 'Aldous Huxley',
                'genre': 'Dystopian',
                'year': 1932,
                'review': 'WIP',
            },
        ]
    }
    return render(request, 'main/books.html', values)



def about(request):
    return render(request, 'main/about.html')


def aboutproject(request):
    return render(request, 'main/aboutproject.html')

def contact(request):
    return render(request, 'main/contact.html')

def forum_home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'forum/forum_home.html', {'posts': posts})
