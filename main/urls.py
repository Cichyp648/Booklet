# Plik do zarządzania ścieżkami w aplikacji. Zawiera listę ścieżek powiązanych z widokami.

from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('books/', include('books.urls')),
    path('movies/', include('movies.urls')),
    path('about/', views.about, name='about'),
    path('aboutproject/', views.aboutproject, name='project'),
    path('contact/', views.contact, name='contact'),
    path('forum/', include('forum.urls'))
]
