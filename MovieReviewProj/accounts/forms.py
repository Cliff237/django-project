from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Accounts


class createAccountForms(UserCreationForm):
    class Meta:
        model = Accounts
        fields = ['name', 'email', 'password1', 'password2']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Accounts.objects.filter(username=email).exists():
            raise forms.ValidationError(
                "An account with this email already exists.")
        return email
