from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
        return f"Movie name: {self.title}, Description: {self.description}, Duration: {self.duration}min."
