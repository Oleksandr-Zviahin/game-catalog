from django.db import models
from rest_framework import serializers


class Platform(models.Model):
    platform_name = models.CharField(max_length=100)
    platform_version = models.CharField(max_length=30)
    platform_description = models.CharField(max_length=1500)

    def __str__(self):
        return "%s: %s" % (self.platform_name, self.platform_version)


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        fields = (
            'platform_name',
            'platform_version',
            'platform_description',
        )