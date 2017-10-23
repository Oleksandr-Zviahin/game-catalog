from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=40)
    category_description = models.CharField(max_length=1500)

    def __str__(self):
        return self.category_name
