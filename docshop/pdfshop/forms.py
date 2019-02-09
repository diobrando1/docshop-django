"""
pdfshop forms
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """Represents user creation form"""
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        """Meta class"""
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )

class UploadFileForm(forms.Form):
    """Represents file upload form"""
    title = forms.CharField(max_length=50, help_text='Required. Name with max 50 characters')
    file = forms.FileField(help_text='Required. Choose your PDF file')
