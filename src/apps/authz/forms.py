from django.core.validators import RegexValidator
from django import forms

# Validator to enforce alpha-numeric usernames
alphan_validator = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class UsernamePasswordForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=32,
        validators=[alphan_validator],
        required=True,
        error_messages={
            'required': 'Username is required.',
            'min_length': 'Username must be at least 3 characters long.',
            'max_length': 'Username cannot exceed 32 characters.',
            'invalid': 'Username must contain only alphanumeric characters.'
        }
    )
    
    password = forms.CharField(
        min_length=6,
        max_length=32,
        widget=forms.PasswordInput(),
        required=True,
        error_messages={
            'required': 'Password is required.',
            'min_length': 'Password must be at least 6 characters long.',
            'max_length': 'Password cannot exceed 32 characters.'
        }
    )