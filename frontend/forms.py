from django.forms import ModelForm

from .models import Sound


class SoundForm(ModelForm):
    class Meta:
        model = Sound
        fields = "__all__"
