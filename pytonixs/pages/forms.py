from django import forms
from .models import NewClient

class ContactForm(forms.ModelForm):
    class Meta:
        model = NewClient
        fields = '__all__'