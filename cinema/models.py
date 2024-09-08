from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    class Meta:
<<<<<<< HEAD
        verbose_name_plural = "movies"

    def __str__(self):
        return f"Movie title: {self.title}, id = {self.id}"
=======
        verbose_name_plural = 'Movies'

    def __str__(self):
        return f"Movie name: {self.title}, Description: {self.description}, Duration: {self.duration}min."
>>>>>>> 2cbd38e98bf9e3beb2278a50632a598be398814d
