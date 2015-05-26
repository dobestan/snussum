from django.db import models
from django.contrib.postgres.fields import IntegerRangeField, ArrayField

from django.db.models.signals import post_save

from django.contrib.auth.models import User
from relationships.models.dating import Dating
from users.models.university import University

from users.tasks.password import send_password_reset_sms, \
    send_password_reset_email
from users.tasks.verification import send_phonenumber_verification_sms, \
    send_university_verification_email

from users.utils.hashids import get_encoded_user_profile_hashid

from datetime import date
from hashlib import sha1
from random import random
import datetime

from django.templatetags.static import static


class UserProfileManager(models.Manager):

    def users(self):
        return User.objects.all()

    def boys(self):
        return self.users().filter(userprofile__is_boy=True)

    def girls(self):
        return self.users().filter(userprofile__is_boy=False)

    def users_university_verified(self):
        return self.users().filter(userprofile__is_university_verified=True)

    def boys_university_verified(self):
        return self.boys().filter(userprofile__is_university_verified=True)

    def girls_university_verified(self):
        return self.girls().filter(userprofile__is_university_verified=True)

    def users_profile_verified(self):
        return self.users_university_verified().filter(
            userprofile__is_boy__isnull=False,
            userprofile__nickname__isnull=False,
            userprofile__profile_introduce__isnull=False,
        )

    def boys_profile_verified(self):
        return self.boys_university_verified().filter(
            userprofile__nickname__isnull=False,
            userprofile__profile_introduce__isnull=False,
        )

    def girls_profile_verified(self):
        return self.girls_university_verified().filter(
            userprofile__nickname__isnull=False,
            userprofile__profile_introduce__isnull=False,
        )

    def users_joined_today(self):
        return self.users().filter(
            date_joined__range=(datetime.date.today(), datetime.date.today() + datetime.timedelta(1))
        )

    def boys_joined_today(self):
        return self.boys().filter(
            date_joined__range=(datetime.date.today(), datetime.date.today() + datetime.timedelta(1))
        )

    def girls_joined_today(self):
        return self.girls().filter(
            date_joined__range=(datetime.date.today(), datetime.date.today() + datetime.timedelta(1))
        )

    def users_joined_yesterday(self):
        return self.users().filter(
            date_joined__range=(datetime.date.today() - datetime.timedelta(1), datetime.date.today())
        )

    def boys_joined_yesterday(self):
        return self.boys().filter(
            date_joined__range=(datetime.date.today() - datetime.timedelta(1), datetime.date.today())
        )

    def girls_joined_yesterday(self):
        return self.girls().filter(
            date_joined__range=(datetime.date.today() - datetime.timedelta(1), datetime.date.today())
        )

    def randomized_profile_verified_boys(self):
        return self.boys_profile_verified().order_by("?")

    def randomized_profile_verified_girls(self):
        return self.girls_profile_verified().order_by("?")

    def _is_boys_more_than_girls(self):
        return self.boys_profile_verified().count() >= self.girls_profile_verified().count()

    def divide_groups(self):
        """
        return (Bigger, Smaller)
        """
        if self._is_boys_more_than_girls():
            return (self.randomized_profile_verified_boys(), self.randomized_profile_verified_girls())
        return (self.randomized_profile_verified_girls(), self.randomized_profile_verified_boys())


def _profile_image_upload_to(instance, filename):
    return "profile/%s" % instance.hash_id + \
        "-" + sha1(str(random()).encode('utf-8')).hexdigest()[:8] + \
        "." + filename.split(".")[-1]


class UserProfile(models.Model):
    objects = UserProfileManager()

    user = models.OneToOneField(User, unique=True, primary_key=True)
    hash_id = models.CharField(max_length=8, unique=True, blank=True, null=True)

    nickname = models.CharField(max_length=8, blank=True, null=True, unique=True)
    is_boy = models.NullBooleanField(default=None, blank=True, null=True)

    # University Validation ( Email Validation )
    university = models.ForeignKey(University, blank=True, null=True)
    is_university_verified = models.BooleanField(default=False)
    university_verification_token = models.CharField(max_length=32, null=True, blank=True)

    # MySNU Username, SNULife Username - 멀티계정 방지
    mysnu_username = models.CharField(max_length=16, blank=True, null=True, unique=True)
    snulife_username = models.CharField(max_length=16, blank=True, null=True, unique=True)

    # PhoneNumber Validation
    phonenumber = models.CharField(max_length=13, default=None, blank=True, null=True, unique=True)
    is_phonenumber_verified = models.BooleanField(default=False)
    phonenumber_verification_token = models.CharField(max_length=32, null=True, blank=True)

    profile_introduce = models.TextField(blank=True, null=True)

    profile_image = models.ImageField(upload_to=_profile_image_upload_to, blank=True, null=True)

    is_dating_enabled = models.BooleanField(default=True)

    # Introduce
    age = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    REGION_CHOICES = (
        # 국내
        ('서울', '서울특별시'),
        ('부산', '부산광역시'),
        ('인천', '인천광역시'),
        ('대구', '대구광역시'),
        ('광주', '광주광역시'),
        ('대전', '대전광역시'),
        ('울산', '울산광역시'),
        ('경기', '경기도'),
        ('강원', '강원도'),
        ('충북', '충청북도'),
        ('충남', '충청남도'),
        ('경북', '경상북도'),
        ('경남', '경상남도'),
        ('전북', '전라북도'),
        ('전남', '전라남도'),
        ('제주', '제주도'),

        # 해외
        ('미국', '미국'),
        ('중국', '중국'),
        ('일본', '일본'),

        # 기타
        ('절망', '절망의땅301동'),
        ('멸망', '멸망의땅301동'),
        ('슬픔', '슬픔의땅301동'),
        ('좌절', '좌절의땅301동'),
    )
    region = models.CharField(max_length=2, choices=REGION_CHOICES, blank=True, null=True)

    # Condition
    age_condition = IntegerRangeField(blank=True, null=True)
    height_condition = IntegerRangeField(blank=True, null=True)
    weight_condition = IntegerRangeField(blank=True, null=True)
    region_condition = ArrayField(models.CharField(max_length=2), blank=True, null=True)

    def _profile_image_url(self):
        if self.profile_image:
            return self.profile_image.url

        if self.is_boy:
            return static('img/profile/boy.jpg')
        else:
            return static('img/profile/girl.jpg')
    profile_image_url = property(_profile_image_url)

    def _is_profile_verified(self):
        if self.is_boy is not None and \
                self.nickname and \
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
            self.is_height_condition_available_with(partner) and \
            self.is_region_condition_available_with(partner)

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

    def is_region_condition_available_with(self, partner):
        if not self.region_condition:
            return True
        elif self.region_condition and not partner.userprofile.region:
            return False
        elif partner.userprofile.region in self.region_condition:
            return True
        else:
            return False

    def create_dating_with(self, partner):
        if self.is_boy:
            return Dating.objects.create(boy=self.user, girl=partner)
        return Dating.objects.create(boy=partner, girl=self.user)

    def update_conditions(self, is_dating_enabled=True, min_age=None, max_age=None,
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
        send_phonenumber_verification_sms.delay(self.pk)

    def update_university(self, email_username, university):
        self.university = university
        self.user.email = email_username + "@" + university.email

        self.is_university_verified = False
        self.update_university_verification_token()

        self.user.save()
        self.save()

        send_university_verification_email(self.user.id)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create UserProfile ( Additional User Information )
        user_profile = UserProfile.objects.create(user=instance)

        user_profile.hash_id = get_encoded_user_profile_hashid(user_profile.pk)
        user_profile.save()

post_save.connect(create_user_profile, sender=User)
