from django.db import models

class Movie(models.Model):
    title = models.CharField("Tytuł",max_length=200)
    director = models.CharField("Reżyser",max_length=100)
    rating = models.FloatField("Ocena")
    genre = models.CharField("Gatunek",max_length=100, default='Brak')

    def __str__(self):
        return f"{self.title} ({self.director})"
