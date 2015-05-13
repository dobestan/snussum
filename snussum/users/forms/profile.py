from django.forms import ModelForm
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
