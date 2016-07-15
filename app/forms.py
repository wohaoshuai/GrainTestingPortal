"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import User_mod, Reports
from django.contrib.auth.models import User

class Signup(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class sign_up_acc(forms.ModelForm):

    class Meta:
        model = User_mod
        fields = ('address', 'city', 'state', 'zipcode')


class report2(forms.ModelForm):

    class Meta:
        model = Reports
        fields = ('ptype', 'min_price', 'max_price', 'date', 'available', 'quantity', 'id1')


# class BootstrapAuthenticationForm(AuthenticationForm):
#     """Authentication form which uses boostrap CSS."""
#     username = forms.CharField(max_length=254,
#                                widget=forms.TextInput({
#                                    'class': 'form-control',
#                                    'placeholder': 'User name'}))
#     password = forms.CharField(label=_("Password"),
#                                widget=forms.PasswordInput({
#                                    'class': 'form-control',
#                                    'placeholder':'Password'}))
