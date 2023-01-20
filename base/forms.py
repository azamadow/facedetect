from django import forms
from .models import Detect


class DetectForm(forms.ModelForm):
    class Meta:
        model = Detect
        fields = ['name', 'surname', 'photo', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),

        }
