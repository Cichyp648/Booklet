from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)

    review_count = models.IntegerField(default=0)
    review_sum = models.IntegerField(default=0)

    def average_rating(self):
        if self.review_count == 0:
            return None
        return round(self.review_sum / self.review_count, 1)
