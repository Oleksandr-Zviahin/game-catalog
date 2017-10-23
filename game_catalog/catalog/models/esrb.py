from django.db import models


class ESRB(models.Model):
    rate_full_name = models.CharField(max_length=50)
    rate_short_name = models.CharField(max_length=10)
    rate_description = models.CharField(max_length=1500)

    def __str__(self):
        return self.rate_full_name
