from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def index(request):
    books = Book.objects.all()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_index')  # Must match your URL name
    else:
        form = BookForm()

    return render(request, 'books/index.html', {'form': form, 'books': books})
