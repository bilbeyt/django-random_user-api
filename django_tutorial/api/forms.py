from django import forms
from api.models import Student


class TalentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = []