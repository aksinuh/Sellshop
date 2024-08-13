from typing import Any
from django.contrib.auth import get_user_model
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
import re

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    confirim_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        "placeholder": "Confirim password"
    }))
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone_number',
            'password'
        )
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Phone Number'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password'
            }),
        }
        
        
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            if len(password) < 6:
                raise ValidationError('Password must be 6 characters long.')
            if not (password.isalnum() and not password.isalpha() and not password.isdigit()):
                raise ValidationError('Password must consist of both letters and numbers.')
        return password 

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirim_password = cleaned_data.get("confirim_password")

        if password and confirim_password and password != confirim_password:
            raise forms.ValidationError("Passwords must be the same")
    
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise ValidationError('Email must be a gmail.com address.')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError('Phone number already exists.')
        return phone_number


    # def clean_number(self):
    #     phone_number = self.cleaned_data.get('phone_number')
    #     if phone_number == phone_number:
    #         raise forms.ValidationError("phone_number must be same")
    #     return phone_number
    
    
class LoginForm(forms.Form):
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        
        "placeholder": "Email",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        
        "placeholder": "Password"
    }))



    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise ValidationError('Invalid email or password')
        return cleaned_data