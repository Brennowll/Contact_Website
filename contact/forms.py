from django import forms
from contact import models

class ContactForm(forms.ModelForm):
    class Meta: 
        model = models.Contact
        fields = [
                'name',
                'phone',
                'email',
                'address',
        ]