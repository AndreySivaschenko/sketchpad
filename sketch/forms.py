from django.forms import forms
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