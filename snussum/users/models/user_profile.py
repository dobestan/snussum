from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import User


class UserProfileManager(models.Manager):
    def boys(self):
        return User.objects.filter(userprofile__is_boy=True)

    def girls(self):
        return User.objects.filter(userprofile__is_boy=False)

    def randomized_boys(self):
        return self.boys().order_by("?")

    def randomized_girls(self):
        return self.girls().order_by("?")


class UserProfile(models.Model):
    objects = UserProfileManager()

    user = models.OneToOneField(User, unique=True, primary_key=True)

    is_boy = models.BooleanField(default=True)

    def _is_girl(self):
        return not is_boy
    is_girl = property(_is_girl)
    
    def __str__(self):
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
