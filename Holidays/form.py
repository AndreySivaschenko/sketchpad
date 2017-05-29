from django import forms

from Holidays.models import holidays


class AnalysisForm(forms.ModelForm):
    class Meta:
        model = holidays
        fields = ['holidays_name','holidays_description','holidays_date']