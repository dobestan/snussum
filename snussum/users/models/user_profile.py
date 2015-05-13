from django.db import models
from django.contrib.postgres.fields import IntegerRangeField

from django.db.models.signals import post_save

from django.contrib.auth.models import User
from relationships.models.dating import Dating
from users.models.university import University

from users.tasks.password import send_password_reset_sms, \
    send_password_reset_email

from users.utils.hashids import get_encoded_user_profile_hashid

from datetime import date
from hashlib import sha1
from random import random

from django.templatetags.static import static


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
    return "profile/%s" % instance.hash_id + \
        "-" + sha1(str(random()).encode('utf-8')).hexdigest()[:8] + \
        "." + filename.split(".")[-1]


class UserProfile(models.Model):
    objects = UserProfileManager()

    user = models.OneToOneField(User, unique=True, primary_key=True)
    hash_id = models.CharField(max_length=8, unique=True, blank=True, null=True)

    nickname = models.CharField(max_length=8, blank=True, null=True, unique=True)
    is_boy = models.BooleanField(default=True)

    # University Validation ( Email Validation )
    university = models.ForeignKey(University, blank=True, null=True)
    is_university_verified = models.BooleanField(default=False)
    university_verification_token = models.CharField(max_length=32, null=True, blank=True)

    # PhoneNumber Validation
    phonenumber = models.CharField(max_length=11, blank=True, null=True, unique=True)
    is_phonenumber_verified = models.BooleanField(default=False)
    phonenumber_verification_token = models.CharField(max_length=32, null=True, blank=True)

    profile_introduce = models.TextField(blank=True, null=True)

    profile_image = models.ImageField(upload_to=_profile_image_upload_to, blank=True, null=True)

    is_dating_enabled = models.BooleanField(default=True)

    # Introduce
    age = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    # Condition
    age_condition = IntegerRangeField(blank=True, null=True)
    height_condition = IntegerRangeField(blank=True, null=True)
    weight_condition = IntegerRangeField(blank=True, null=True)

    def _profile_image_url(self):
        if self.profile_image:
            return self.profile_image.url

        if self.is_boy:
            return static('img/profile/boy.jpg')
        else:
            return static('img/profile/girl.jpg')
    profile_image_url = property(_profile_image_url)

    def _is_profile_verified(self):
        if self.nickname and \
                self.profile_introduce and len(self.profile_introduce) >= 50:
            return True
        return False
    is_profile_verified = property(_is_profile_verified)

    def _is_girl(self):
        return not is_boy
    is_girl = property(_is_girl)

    def __str__(self):
        return self.user.username

    def _get_social_auth_profile(self, provider):
        return self.user.social_auth.filter(provider=provider).first()

    def facebook(self):
        return self._get_social_auth_profile("facebook")

    def kakao(self):
        return self._get_social_auth_profile("kakao")

    def reset_password(self):
        new_password = sha1(str(random()).encode('utf-8')).hexdigest()[:6]
        self.user.set_password(new_password)
        self.user.save()

        send_password_reset_sms(self.user, new_password)
        send_password_reset_email(self.user, new_password)

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
        """
        매칭이 가능한지 여부를 파악한다.

        1. 기본 조건 검사 ( 기존 매칭 여부, 당일 매칭 여부 등 )
        2. 나의 조건 - 상대방 프로필 검사
        3. 나의 프로필 - 상대방 조건 검사
        """
        return not self.dating_matched_today() and \
            not partner.userprofile.dating_matched_today() and \
            not self.dating_matched_with(partner) and \
            self.is_conditions_available_with(partner) and \
            partner.userprofile.is_conditions_available_with(self.user)

    def is_conditions_available_with(self, partner):
        """
        모든 조건에 부합하는지 검사한다.
        """
        return self.is_age_condition_available_with(partner) and \
            self.is_height_condition_available_with(partner)

    def is_age_condition_available_with(self, partner):
        # 나이 조건에 상대방의 나이가 적합한지 확인한다.

        if not self.age_condition:
            # 나이 조건이 설정되지 않았다면 ( UserProfile Default )
            # 상대방의 나이와 상관 없이 True를 반환한다.
            return True
        elif self.age_condition and not partner.userprofile.age:
            # 나이 조건이 설정되었으나 상대방의 나이가 없는 경우
            return False
        elif partner.userprofile.age in self.age_condition:
            # 나이 조건이 설정되었고,
            # 상대방의 나이가 있는 경우,
            # 나이 조건에 상대방의 나이가 포함된다면 True를 반환한다.
            return True
        else:
            # 나이 조건에 상대방의 나이가 포함되지 않는다면 True를 반환한다.
            return False

    def is_height_condition_available_with(self, partner):
        if not self.height_condition:
            return True
        elif self.height_condition and not partner.userprofile.height:
            return False
        elif partner.userprofile.height in self.height_condition:
            return True
        else:
            return False

    def is_weight_condition_available_with(self, partner):
        pass

    def create_dating_with(self, partner):
        if self.is_boy:
            return Dating.objects.create(boy=self.user, girl=partner)
        return Dating.objects.create(boy=partner, girl=self.user)

    def update_conditions(self, is_dating_enabled=True, min_age=None, max_age=None, \
            min_height=None, max_height=None):
        self.is_dating_enabled = is_dating_enabled

        self.age_condition = (min_age, max_age)
        self.height_condition = (min_height, max_height)
        self.save()

    def generate_verification_token(self):
        salt = sha1(str(random()).encode('utf-8')).hexdigest()[:5]
        university_verification_token = sha1((self.user.username + salt).encode('utf-8')).hexdigest()[:32]
        return university_verification_token

    def update_university_verification_token(self):
        university_verification_token = self.generate_verification_token()
        self.university_verification_token = university_verification_token
        self.save()

    def update_phonenumber_verification_token(self):
        phonenumber_verification_token = self.generate_verification_token()
        self.phonenumber_verification_token = phonenumber_verification_token
        self.save()

    def update_phonenumber(self, phonenumber):
        self.phonenumber = phonenumber

        self.is_phonenumber_verified = False
        self.update_phonenumber_verification_token()

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
