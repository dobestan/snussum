from django.forms import ModelForm
from relationships.models.self_dating import SelfDating

from django_summernote.widgets import SummernoteWidget


class SelfDatingForm(ModelForm):
    class Meta:
        model = SelfDating
        exclude = []
        widgets = {
            'content': SummernoteWidget(),
        }
