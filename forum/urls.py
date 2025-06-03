from django.urls import path
from . import views # from current folder import the neighbour file views for views methods usage

urlpatterns = [
    path('', views.index),
    path('', views.index, name='index'),
    path('create/', views.index, name='index'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('frequent_questions', views.frequent_questions)
]
 