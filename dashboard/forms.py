from django import forms
from .models import acase


class AddCaseForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = acase
        fields = ('firstname','lastname', 'image','address','landmark','locality','city','district','state','zipcode')