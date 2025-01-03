from django import forms
from .models import Suspect


class SuspectForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Suspect
        fields = ('landmark','locality','city','district','state','zipcode', 'image')