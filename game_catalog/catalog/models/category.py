from django.db import models
from rest_framework import serializers


class Category(models.Model):
    category_name = models.CharField(max_length=40)
    category_description = models.CharField(max_length=1500)

    def __str__(self):
        return self.category_name


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name', 'category_description')
