from django.conf import settings
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from userprofile.models import UserProfile
from .models import Note


class AnalysisForm(forms.ModelForm):
    notes_title = forms.CharField(max_length=50)
    notes_description = forms.CharField(widget=forms.Textarea)
    notes_time = forms.TimeField(input_formats=['H:i'])
    notes_date = forms.DateField(input_formats=['%d.%m.%Y'])
    notes_priority = forms.IntegerField(max_value=4,min_value=0)

    class Meta:
        model = Note
        fields = ['notes_title','notes_description','notes_time','notes_date','notes_priority']



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
        ]

class EditProfileMoreForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['dateBirth','phone','avatar']



