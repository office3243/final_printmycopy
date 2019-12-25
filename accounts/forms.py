from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from . models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import password_validation

USER_MODEL = User


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=13, widget=forms.TextInput(attrs={"class": "input-medium bfh-phone", "data-format": "+91dddddddddd"}))


class RegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=13, widget=forms.TextInput(attrs={"class": "input-medium bfh-phone", "data-format": "+91dddddddddd"}))

    class Meta:
        model = User
        fields = ('phone', 'email', 'password1', 'password2',)


class OTPForm(forms.Form):
    otp = forms.IntegerField(widget=forms.NumberInput(attrs={"length": 6}))

    class Meta:
        fields = ('otp', )


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = USER_MODEL
        fields = ('first_name', 'last_name', 'email', 'city', )
