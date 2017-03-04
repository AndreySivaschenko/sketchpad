from django.conf import settings
from django import forms


from .models import Note


class AnalysisForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


    notes_title = forms.CharField(max_length=50)
    notes_description = forms.CharField(widget=forms.Textarea)
    notes_time = forms.TimeField(input_formats=['H:i'])
    notes_date = forms.DateField(input_formats=['%d.%m.%Y'])
    notes_priority = forms.IntegerField(max_value=4)



