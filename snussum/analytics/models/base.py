from django.db import models


class AnalyticsManagerBase(models.Manager):
    def create_analytics(self):
        instance = self.model()
        instance.save()
        return instance


    class Meta:
        abstract = True
