from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save

from analytics.models.base import AnalyticsManagerBase, AnalyticsModelBase

import datetime

from users.models.user_profile import UserProfile
from relationships.models.dating import Dating


class DemographicManager(AnalyticsManagerBase):
    pass


class Demographic(AnalyticsModelBase):
    objects = DemographicManager()

    # Date - 날짜의 경우에는 24시를 기준으로 새롭계 계산하므로 어제의 날짜로 생성
    date = models.DateField(default=datetime.date.today() - datetime.timedelta(1))

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

    def __str__(self):
        return str(self.date)


@receiver(post_save, sender=Demographic)
def _calculate_demographic(sender, instance, created, **kwargs):
    if created:
        instance.users = UserProfile.objects.users().count()
        instance.boys = UserProfile.objects.boys().count()
        instance.girls = UserProfile.objects.girls().count()

        instance.users_university_verified = UserProfile.objects.users_university_verified().count()
        instance.boys_university_verified = UserProfile.objects.boys_university_verified().count()
        instance.girls_university_verified = UserProfile.objects.girls_university_verified().count()

        instance.users_profile_verified = UserProfile.objects.users_profile_verified().count()
        instance.boys_profile_verified = UserProfile.objects.boys_profile_verified().count()
        instance.girls_profile_verified = UserProfile.objects.girls_profile_verified().count()

        instance.users_joined_today = UserProfile.objects.users_joined_yesterday().count()
        instance.boys_joined_today = UserProfile.objects.boys_joined_yesterday().count()
        instance.girls_joined_today = UserProfile.objects.girls_joined_yesterday().count()

        instance.users_dating_matched_today = Dating.objects.datings_matched_yesterday().count()

        instance.save()
