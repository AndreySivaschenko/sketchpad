from django.forms import forms
from .models import comment


class CommentForm(forms.Form):
        class Meta:
            model = comment
            filter = [
                'comment_name',
                'comment_email',
                'comment_date',
                'comment_recall'
            ]
