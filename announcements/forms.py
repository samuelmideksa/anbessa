from django import forms
from django.forms import inlineformset_factory
from .models import Announcement, Image


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['rows'] = 5


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']


ImageFormSet = inlineformset_factory(Announcement, Image, form=ImageForm, extra=3)
