from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.TextField()
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title
