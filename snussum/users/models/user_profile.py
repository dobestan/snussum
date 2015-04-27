from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import User
from relationships.models.dating import Dating
from users.models.university import University

from datetime import date


class UserProfileManager(models.Manager):

    def boys(self):
        return User.objects.filter(userprofile__is_boy=True)

    def girls(self):
        return User.objects.filter(userprofile__is_boy=False)

    def randomized_boys(self):
        return self.boys().order_by("?")

    def randomized_girls(self):
        return self.girls().order_by("?")

    def _is_boys_more_than_girls(self):
        return self.boys().count() >= self.girls().count()

    def divide_groups(self):
        """
        return (Bigger, Smaller)
        """
        if self._is_boys_more_than_girls():
            return (self.randomized_boys(), self.randomized_girls())
        return (self.randomized_girls(), self.randomized_boys())


class UserProfile(models.Model):
    objects = UserProfileManager()

    user = models.OneToOneField(User, unique=True, primary_key=True)

    is_boy = models.BooleanField(default=True)

    university = models.ForeignKey(University, blank=True, null=True)

    def _is_girl(self):
        return not is_boy
    is_girl = property(_is_girl)

    def __str__(self):
        return self.user.username

    def datings_matched(self):
        if self.is_boy:
            return self.user.dating_girls.all()
        return self.user.dating_boys.all()

    def dating_matched_today(self):
        return self.datings_matched().filter(matched_at=date.today()).first()

    def datings_matched_recently_except_today(self):
        return self.datings_matched().exclude(matched_at=date.today())[:3]

    def dating_matched_with(self, partner):
        if self.is_boy:
            return Dating.objects.filter(boy=self.user, girl=partner).first()
        return Dating.objects.filter(boy=partner, girl=self.user).first()

    def is_dating_available_with(self, partner):
        return not self.dating_matched_today() and \
            not partner.userprofile.dating_matched_today() and \
            not self.dating_matched_with(partner)

    def create_dating_with(self, partner):
        if self.is_boy:
            return Dating.objects.create(boy=self.user, girl=partner)
        return Dating.objects.create(boy=partner, girl=self.user)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Initialize Email ( username + mysnu_email )
        instance.email = instance.username + "@snu.ac.kr"
        instance.save()

        # Create UserProfile ( Additional User Information )
        UserProfile.objects.create(user=instance)
        user_profile = instance.userprofile

post_save.connect(create_user_profile, sender=User)
