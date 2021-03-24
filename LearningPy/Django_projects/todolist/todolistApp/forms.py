from datetime import date

from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput, TimeInput, TextInput, SplitHiddenDateTimeWidget

from todolistApp.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'start_date': DateInput(attrs={"type": "date"}),
            'end_date': DateInput(attrs={"type": "date"}),
            'duration': TextInput(attrs={"type": "number", "min": "1", "max":"4"})
        }

    def clean_start_date(self):
        d_start = self.cleaned_data.get('start_date')
        d_end = self.cleaned_data.get('end_date')
        if d_start < date.today():
            raise ValidationError("Meetings cannot start in the past")

        return d_start

    def clean_end_date(self):
        d_start = self.cleaned_data.get('start_date')
        d_end = self.cleaned_data.get('end_date')

        if d_end < date.today():
            raise ValidationError("Meetings cannot end in the past")

        if d_end < d_start:
            raise ValidationError("End date cannot be before start date")

        return d_end

