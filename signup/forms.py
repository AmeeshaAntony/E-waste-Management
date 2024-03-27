# forms.py

from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Assuming these are your model fields
        widgets = {
            'password': forms.PasswordInput()
        }
