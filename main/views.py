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


def movies(request):
    values = {
        'movies': [
        {
            'title': 'The Lord of the Rings: The Fellowship of the Ring',
            'director': 'Peter Jackson',
            'genre': 'Fantasy',
            'year': 2001,
            'review': 'WIP',
        },
        {
            'title': 'The Lord of the Rings: The Two Towers',
            'director': 'Peter Jackson',
            'genre': 'Fantasy',
            'year': 2002,
            'review': 'WIP',
        },
        {
            'title': 'The Lord of the Rings: The Return of the King',
            'director': 'Peter Jackson',
            'genre': 'Fantasy',
            'year': 2003,
            'review': 'WIP',
        },
        {
            'title': 'The Hobbit: An Unexpected Journey',
            'director': 'Peter Jackson',
            'genre': 'Fantasy',
            'year': 2012,
            'review': 'WIP',
        },
        {
            'title': 'The Hobbit: The Desolation of Smaug',
            'director': 'Peter Jackson',
            'genre': 'Fantasy',
            'year': 2013,
            'review': 'WIP',
        },
        {
            'title': 'The Hobbit: The Battle of the Five Armies',
            'director': 'Peter Jackson',
            'genre': 'Fantasy',
            'year': 2014,
            'review': 'WIP',
        },
        {
            'title': 'Harry Potter and the Philosopher\'s Stone',
            'director': 'Chris Columbus',
            'genre': 'Fantasy',
            'year': 2001,
            'review': 'WIP',
        },
        {
            'title': 'Harry Potter and the Chamber of Secrets',
            'director': 'Chris Columbus',
            'genre': 'Fantasy',
            'year': 2002,
            'review': 'WIP',
        },
        {
            'title': 'Harry Potter and the Prisoner of Azkaban',
            'director': 'Alfonso Cuarón',
            'genre': 'Fantasy',
            'year': 2004,
            'review': 'WIP',
        },
        {
            'title': 'Harry Potter and the Goblet of Fire',
            'director': 'Mike Newell',
            'genre': 'Fantasy',
            'year': 2005,
            'review': 'WIP',
        },
        {
            'title': 'Harry Potter and the Order of the Phoenix',
            'director': 'David Yates',
            'genre': 'Fantasy',
            'year': 2007,
            'review': 'WIP',
        },
        {
            'title': 'Harry Potter and the Half-Blood Prince',
            'director': 'David Yates',
            'genre': 'Fantasy',
            'year': 2009,
            'review': 'WIP',
        },
        {
            'title': 'Harry Potter and the Deathly Hallows: Part 1',
            'director': 'David Yates',
            'genre': 'Fantasy',
            'year': 2010,
            'review': 'WIP',
        },
        {
            'title': 'Harry Potter and the Deathly Hallows: Part 2',
            'director': 'David Yates',
            'genre': 'Fantasy',
            'year': 2011,
            'review': 'WIP',
        },
        {
            'title': 'Star Wars: Episode IV - A New Hope',
            'director': 'George Lucas',
            'genre': 'Science Fiction',
            'year': 1977,
            'review': 'WIP',
        },
        {
            'title': 'Star Wars: Episode V - The Empire Strikes Back',
            'director': 'Irvin Kershner',
            'genre': 'Science Fiction',
            'year': 1980,
            'review': 'WIP',
        },
        {
            'title': 'Star Wars: Episode VI - Return of the Jedi',
            'director': 'Richard Marquand',
            'genre': 'Science Fiction',
            'year': 1983,
            'review': 'WIP',
        },
        {
            'title': 'Star Wars: Episode I - The Phantom Menace',
            'director': 'George Lucas',
            'genre': 'Science Fiction',
            'year': 1999,
            'review': 'WIP',
        },
        {
            'title': 'Star Wars: Episode II - Attack of the Clones',
            'director': 'George Lucas',
            'genre': 'Science Fiction',
            'year': 2002,
            'review': 'WIP',
        },
        {
            'title': 'Star Wars: Episode III - Revenge of the Sith',
            'director': 'George Lucas',
            'genre': 'Science Fiction',
            'year': 2005,
            'review': 'WIP',
        },
        {
            'title': 'Inception',
            'director': 'Christopher Nolan',
            'genre': 'Science Fiction',
            'year': 2010,
            'review': 'WIP',
        },
        {
            'title': 'Interstellar',
            'director': 'Christopher Nolan',
            'genre': 'Science Fiction',
            'year': 2014,
            'review': 'WIP',
        },
        {
            'title': 'The Dark Knight',
            'director': 'Christopher Nolan',
            'genre': 'Superhero',
            'year': 2008,
            'review': 'WIP',
        },
        {
            'title': 'The Dark Knight Rises',
            'director': 'Christopher Nolan',
            'genre': 'Superhero',
            'year': 2012,
            'review': 'WIP',
        },
        {
            'title': 'Batman Begins',
            'director': 'Christopher Nolan',
            'genre': 'Superhero',
            'year': 2005,
            'review': 'WIP',
        },
        {
            'title': 'The Matrix',
            'director': 'The Wachowskis',
            'genre': 'Science Fiction',
            'year': 1999,
            'review': 'WIP',
        },
        {
            'title': 'The Matrix Reloaded',
            'director': 'The Wachowskis',
            'genre': 'Science Fiction',
            'year': 2003,
            'review': 'WIP',
        },
        {
            'title': 'The Matrix Revolutions',
            'director': 'The Wachowskis',
            'genre': 'Science Fiction',
            'year': 2003,
            'review': 'WIP',
        },
        {
            'title': 'Dune: Part One',
            'director': 'Denis Villeneuve',
            'genre': 'Science Fiction',
            'year': 2021,
            'review': 'WIP',
        },
        {
            'title': 'Dune: Part Two',
            'director': 'Denis Villeneuve',
            'genre': 'Science Fiction',
            'year': 2024,
            'review': 'WIP',
        },
        {
            'title': 'Avatar',
            'director': 'James Cameron',
            'genre': 'Science Fiction',
            'year': 2009,
            'review': 'WIP',
        },
        {
            'title': 'Avatar: The Way of Water',
            'director': 'James Cameron',
            'genre': 'Science Fiction',
            'year': 2022,
            'review': 'WIP',
        },
        {
            'title': 'Jurassic Park',
            'director': 'Steven Spielberg',
            'genre': 'Science Fiction',
            'year': 1993,
            'review': 'WIP',
        },
        {
            'title': 'The Lost World: Jurassic Park',
            'director': 'Steven Spielberg',
            'genre': 'Science Fiction',
            'year': 1997,
            'review': 'WIP',
        },
        {
            'title': 'Jurassic World',
            'director': 'Colin Trevorrow',
            'genre': 'Science Fiction',
            'year': 2015,
            'review': 'WIP',
        },
        {
            'title': 'Back to the Future',
            'director': 'Robert Zemeckis',
            'genre': 'Science Fiction',
            'year': 1985,
            'review': 'WIP',
        },
        {
            'title': 'Back to the Future Part II',
            'director': 'Robert Zemeckis',
            'genre': 'Science Fiction',
            'year': 1989,
            'review': 'WIP',
        },
        {
            'title': 'Back to the Future Part III',
            'director': 'Robert Zemeckis',
            'genre': 'Science Fiction',
            'year': 1990,
            'review': 'WIP',
        },
        {
            'title': 'Blade Runner',
            'director': 'Ridley Scott',
            'genre': 'Science Fiction',
            'year': 1982,
            'review': 'WIP',
        },
        {
            'title': 'Blade Runner 2049',
            'director': 'Denis Villeneuve',
            'genre': 'Science Fiction',
            'year': 2017,
            'review': 'WIP',
        },
    ]
    }

    return render(request, 'main/movies.html', values)


def about(request):
    return render(request, 'main/about.html')


def aboutproject(request):
    return render(request, 'main/aboutproject.html')

def contact(request):
    return render(request, 'main/contact.html')
