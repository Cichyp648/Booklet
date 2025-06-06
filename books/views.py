from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm, ReviewForm

def index(request):
    books = Book.objects.all()

    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        rating = int(request.POST.get('rating'))
        try:
            book = Book.objects.get(id=book_id)
            book.review_count += 1
            book.review_sum += rating
            book.save()
            return redirect('book_index')
        except Book.DoesNotExist:
            pass  # Optionally handle this error

    return render(request, 'books/index.html', {'books': books})

