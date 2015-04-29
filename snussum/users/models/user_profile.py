from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import User
from relationships.models.dating import Dating
from users.models.university import University

from users.utils.hashids import get_encoded_user_profile_hashid

from datetime import date
from hashlib import sha1
from random import random


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


def _profile_image_upload_to(instance, filename):
    return "profile/%s" % instance.hash_id + "." + filename.split(".")[-1]
        

class UserProfile(models.Model):
    objects = UserProfileManager()

    user = models.OneToOneField(User, unique=True, primary_key=True)
    hash_id = models.CharField(max_length=8, unique=True, blank=True, null=True)

    is_boy = models.BooleanField(default=True)

    university = models.ForeignKey(University, blank=True, null=True)
    is_university_verified = models.BooleanField(default=False)
    university_verification_token = models.CharField(max_length=32, null=True, blank=True)

    nickname = models.CharField(max_length=8, blank=True, null=True, unique=True)
    profile_introduce = models.TextField(blank=True, null=True)

    profile_image = models.ImageField(upload_to=_profile_image_upload_to, blank=True, null=True)

    def _is_profile_verified(self):
        if self.nickname and \
                self.profile_introduce:
            return True
        return False
    is_profile_verified = property(_is_profile_verified)

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

    def generate_university_verification_token(self):
        salt = sha1(str(random()).encode('utf-8')).hexdigest()[:5]
        university_verification_token = sha1((self.user.username + salt).encode('utf-8')).hexdigest()[:32]
        return university_verification_token

    def update_university_verification_token(self):
        university_verification_token = self.generate_university_verification_token()
        self.university_verification_token = university_verification_token
        self.save()

    def update_university(self, email_username, university):
        """
        1. Update University
        2. Update Email ( with university public email address )
        3. Reset University Verified to False
        4. Send Verification Email
        """
        self.university = university
        self.user.email = email_username + "@" + university.email

        self.is_university_verified = False
        self.update_university_verification_token()

        self.user.save()
        self.save()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create UserProfile ( Additional User Information )
        user_profile = UserProfile.objects.create(user=instance)

        user_profile.hash_id = get_encoded_user_profile_hashid(user_profile.pk)
        user_profile.save()

post_save.connect(create_user_profile, sender=User)
