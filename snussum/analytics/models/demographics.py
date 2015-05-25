from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save

from analytics.models.base import AnalyticsManagerBase, AnalyticsModelBase

import datetime


class DemographicsManager(AnalyticsManagerBase):
    pass


class Demographics(AnalyticsModelBase):
    objects = DemographicsManager()

    # Date - 날짜의 경우에는 24시를 기준으로 새롭계 계산하므로 어제의 날짜로 생성
    date = models.DateField(default=datetime.date.today()-datetime.timedelta(1))


    # Basic Demographics
    users = models.IntegerField(blank=True, null=True)
    boys = models.IntegerField(blank=True, null=True)
    girls = models.IntegerField(blank=True, null=True)

    # Basic Demographics with University Verified
    users_university_verified = models.IntegerField(blank=True, null=True)
    boys_university_verified = models.IntegerField(blank=True, null=True)
    girls_university_verified = models.IntegerField(blank=True, null=True)

    # Basic Demographics with Profile Verified
    # - including is_boy, nickname, profile_introduce
    users_profile_verified = models.IntegerField(blank=True, null=True)
    boys_profile_verified = models.IntegerField(blank=True, null=True)
    girls_profile_verified = models.IntegerField(blank=True, null=True)


    # New Registered Deomographics
    users_joined_today = models.IntegerField(blank=True, null=True)
    boys_joined_today = models.IntegerField(blank=True, null=True)
    girls_joined_today = models.IntegerField(blank=True, null=True)


    # Datings Matched Demographics
    users_dating_matched_today = models.IntegerField(blank=True, null=True)
    boys_dating_matched_today = models.IntegerField(blank=True, null=True)
    girls_dating_matched_today = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return str(self.date)


@receiver(post_save, sender=Demographics)
def _calculate_demographics(sender, instance, created, **kwargs):
    if created:
        instance.save()
