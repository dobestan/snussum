from django.forms import ModelForm

from django.contrib.auth.models import User
from users.models.user_profile import UserProfile

from django_summernote.widgets import SummernoteInplaceWidget


class UserProfileInformationForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = [
            'nickname',
            'profile_introduce',
            'age',
            'height',
        ]
        widgets = {
            'profile_introduce': SummernoteInplaceWidget(),
        }


class UserProfileAccountPhonenumberForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ['phonenumber']


class UserProfileAccountEmailForm(ModelForm):
    
    class Meta:
        model = User
        fields = ['email']
