from django.db import models
from rest_framework import serializers

from .category import Category, CategorySerializer
from .esrb import ESRB, ESRBSerializer
from .genre import Genre, GenreSerializer
from .platform import Platform, PlatformSerializer


class Game(models.Model):
    game_name = models.CharField(max_length=200)
    game_company = models.CharField(max_length=100)
    game_description = models.CharField(max_length=1500)
    game_release_date = models.DateField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    esrb_id = models.ForeignKey(ESRB, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    platforms = models.ManyToManyField(Platform)

    def __str__(self):
        return self.game_name


class GameSerializer(serializers.HyperlinkedModelSerializer):
    category_id = CategorySerializer(read_only=True, many=False)
    esrb_id = ESRBSerializer(read_only=True, many=False)
    genres = GenreSerializer(read_only=True, many=True)
    platforms = PlatformSerializer(read_only=True, many=True)

    class Meta:
        model = Game
        fields = (
            'game_name',
            'game_company',
            'game_description',
            'game_release_date',
            'category_id',
            'esrb_id',
            'genres',
            'platforms',
        )