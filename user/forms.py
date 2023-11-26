from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ProfileModel


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username', 'style': 'font-size: 16px; font-weight: 500;  color: black; margin-bottom:12px; border-radius:4px;padding:4px;'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password', 'style': 'font-size: 16px; font-weight: 500;  color: black;margin-bottom:12px;border-radius:4px;padding:4px;'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Your Password', 'style': 'font-size: 16px; font-weight: 500; color: black;margin-bottom:12px;border-radius:4px;padding:4px;'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

Signupformset = forms.formset_factory(form=SignUpForm, extra=1)


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username', 'style': 'font-size: 16px; font-weight: 500;  color: black; margin-bottom:12px; border-radius:4px;padding:4px;'}))
    class Meta:
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['image']

