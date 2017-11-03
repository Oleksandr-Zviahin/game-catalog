from django.db import models
from rest_framework import serializers


class Genre(models.Model):
    genre_name = models.CharField(max_length=50)
    genre_description = models.CharField(max_length=1500)

    def __str__(self):
        return self.genre_name


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre_name', 'genre_description')