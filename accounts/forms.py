from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import PasswordInput


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        """Initialize a user form."""
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password confirmation'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
