from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Contact


class loginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
       


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class':'w-full py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your confirmpassword',
        'class':'w-full py-4 px-6 rounded-xl'
    }))


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class':'w-full py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your password',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Enter your confirmpassword',
        'class':'w-full py-4 px-6 rounded-xl'
    }))