# forms.py

from django import forms
from .models import Update_Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Update_Profile
        fields = ['profile_pic']
