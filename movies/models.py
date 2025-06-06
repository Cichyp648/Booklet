from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.TextField()
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()

    review_count = models.IntegerField(default=0)
    review_sum = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def average_rating(self):
        if self.review_count == 0:
            return None
        return round(self.review_sum / self.review_count, 1)
