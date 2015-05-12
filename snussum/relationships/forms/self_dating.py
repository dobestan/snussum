from django.forms import ModelForm
from relationships.models.self_dating import SelfDating, SelfDatingApply

from django_summernote.widgets import SummernoteWidget


class SelfDatingForm(ModelForm):

    class Meta:
        model = SelfDating
        fields = ['title', 'content', 'tags_myself', 'tags_partner']
        widgets = {
            'content': SummernoteWidget(),
        }


class SelfDatingApplyForm(ModelForm):

    class Meta:
        model = SelfDatingApply
        fields = ['content']
        widgets = {
            'content': SummernoteWidget(),
        }
