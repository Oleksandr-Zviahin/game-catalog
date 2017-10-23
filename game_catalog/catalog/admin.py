from django.contrib import admin

from .models.category import Category
from .models.esrb import ESRB
from .models.platform import Platform
from .models.genre import Genre
from .models.game import Game

# Register your models here.
admin.site.register(Category)
admin.site.register(ESRB)
admin.site.register(Platform)
admin.site.register(Genre)
admin.site.register(Game)