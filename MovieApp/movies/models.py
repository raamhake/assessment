from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.URLField()
    genre = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    year_release = models.IntegerField()
    metacritic_rating = models.DecimalField(max_digits=3, decimal_places=1)
    runtime = models.IntegerField()

    def __str__(self):
        return self.title

class MovieSchedule(models.Model):
    date = models.DateField()
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} - {self.movie.title}'
