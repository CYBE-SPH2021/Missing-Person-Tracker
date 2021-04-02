from django import forms
from .models import acase, camera


class AddCaseForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = acase
        fields = ('firstname','lastname', 'image','address','landmark','locality','city','district','state','zipcode','phoneno')

class CameraForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = camera
        fields = ('ip_address', 'landmark','locality','city','district','state','zipcode')