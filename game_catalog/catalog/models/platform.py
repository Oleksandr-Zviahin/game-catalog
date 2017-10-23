from django.db import models


class Platform(models.Model):
    platform_name = models.CharField(max_length=100)
    platform_version = models.CharField(max_length=30)
    platform_description = models.CharField(max_length=1500)

    def __str__(self):
        return "%s: %s" % (self.platform_name, self.platform_version)
