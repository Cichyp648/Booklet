# Plik do definiowania widoków, które są renderowane za pomocą szablonizatora Jinja oraz wyświetlane w przeglądarce
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def aboutproject(request):
    return render(request, 'main/aboutproject.html')

def contact(request):
    return render(request, 'main/contact.html')

def forum_home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'forum/forum_home.html', {'posts': posts})
