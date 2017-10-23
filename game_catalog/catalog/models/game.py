from django.db import models
from .category import Category
from .esrb import ESRB
from .genre import Genre
from .platform import Platform


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
