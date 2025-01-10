from django import forms
from .models import ContactUs

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(max_length=5000)

    class Meta:
        model = ContactUs
        fields = ['first_name','last_name','email','message']

def __str__(self):
    return "Contact Form"