from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, primary_key=True)

    def __unicode__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Initialize Email ( username + mysnu_email )
        instance.email = instance.username + "@snu.ac.kr"
        instance.save()

        # Create UserProfile ( Additional User Information )
        UserProfile.objects.create(user=instance)
        user_profile = instance.userprofile

post_save.connect(create_user_profile, sender=User)
