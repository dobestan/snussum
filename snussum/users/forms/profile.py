from django.forms import ModelForm

from django.contrib.auth.models import User
from users.models.user_profile import UserProfile

from django_summernote.widgets import SummernoteInplaceWidget


class UserProfileVerificationForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = [
            # Required Fields
            'nickname',
            'is_boy',
            'profile_introduce',

            # Optional Fields
            'age',
            'height',
        ]
        widgets = {
            'profile_introduce': SummernoteInplaceWidget(),
        }


class UserProfileInformationForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = [
            'nickname',
            'profile_introduce',
            'age',
            'height',
            'region',
        ]
        widgets = {
            'profile_introduce': SummernoteInplaceWidget(),
        }


class UserProfileImageForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ['profile_image', ]


class UserProfileAccountPhonenumberForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ['phonenumber']


class UserProfileAccountEmailForm(ModelForm):

    class Meta:
        model = User
        fields = ['email']
