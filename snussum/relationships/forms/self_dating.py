from django.forms import ModelForm
from relationships.models.self_dating import SelfDating


class SelfDatingForm(ModelForm):
    class Meta:
        model = SelfDating
        exclude = []
