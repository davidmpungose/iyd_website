from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class TenantRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = Profile
        fields = ['phone_number']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        tenant = super().save(commit=False)
        tenant = Profile(
            user=user,
            phone_number=self.cleaned_data['phone_number'],
            email=self.cleaned_data['email']
        )
        return tenant

