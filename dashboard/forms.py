from django import forms
from .models import acase, camera, track_vehicle


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

class VehicleForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = track_vehicle
        fields = ('vehicle_no',)