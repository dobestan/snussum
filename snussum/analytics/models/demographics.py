from django.db import models


class Demographics(models.Model):
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

    # Date
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.date
