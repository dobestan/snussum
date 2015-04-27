from django.db import models


class University(models.Model):
    full_name = models.CharField(max_length=16, blank=True, null=True)
    short_name = models.CharField(max_length=8, blank=True, null=True)

    email = models.CharField(max_length=16, blank=True, null=True)
    slug = models.CharField(max_length=8, blank=True, null=True)

    def __str__(self):
        return self.full_name
