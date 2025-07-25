from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['body_weight', 'goal']
        widgets = {
            'body_weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your weight in kg'}),
            'goal': forms.Select(attrs={'class': 'form-control'}),
        }

