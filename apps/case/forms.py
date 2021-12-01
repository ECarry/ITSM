from django.forms import ModelForm
from .models import Case
from django import forms


# Case form class
class CaseForm(ModelForm):
    class Meta:
        model = Case
        exclude = ['response_time', 'complete_time', 'close_time', 'register']

        widgets = {
            'context': forms.TextInput(attrs={'class': 'col-md-6'})
        }
