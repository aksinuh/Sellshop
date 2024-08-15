from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email',
            'message'
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                "style": "margin-bottom: 10px;"
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'message',
                'rows': 2,
                
                
            }),
       
        }