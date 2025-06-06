from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()  # ← TO TU MUSI BYĆ DLA GET

    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'forum/index.html', {'posts': posts, 'form': form})

def frequent_questions(request):
    return render(request,'forum/frequent_questions.html')
