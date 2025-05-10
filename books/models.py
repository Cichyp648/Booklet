from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.TextField()
    genre = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.title
