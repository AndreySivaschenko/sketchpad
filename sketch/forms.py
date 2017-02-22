from django.conf import settings
from django.forms import forms, DateField, ModelForm


from .models import Note


class AddForm(forms.Form):
        class Meta:
            model = Note
            filter = [
                'notes_title',
                'notes_description',
                'notes_date',
                'notes_priority'
            ]


class DateFormat(ModelForm):
    notes_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
       model = Note