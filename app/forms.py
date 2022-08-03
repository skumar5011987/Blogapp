from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import Post
from django.utils.translation import gettext, gettext_lazy as _


class SigninForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control bg-light', 'placeholder': 'Enter your E-mail'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control bg-light', 'placeholder': 'Enter your password'}))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control bg-light my-1', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control bg-light my-1', 'placeholder': 'Confirm password'}))
    
    class Meta:
        model = User
        fields = ['username','email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control bg-light my-1', 'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-light my-1','placeholder': 'Enter your e-mail'}),
                        
        }


class UserPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','uname', 'author', 'location', 'description']

        labels = {'title': 'Blog title','uname':'Username', 'author': "Enter your name"}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control bg-light my-1', 'placeholder': 'Enter title of you blog'}),
            'uname': forms.TextInput(attrs={'class': 'form-control bg-light my-1', 'placeholder': 'Enter username'}),
            'author': forms.TextInput(attrs={'class': 'form-control bg-light my-1', 'placeholder': 'Enter author name'}),
            # 'date': forms.DateTimeInput(attrs={'class': 'form-control bg-light-1', 'type': 'date', 'placeholder': "Enter Blog's Tital"}),
            'location': forms.TextInput(attrs={'class': 'form-control bg-light my-1', 'placeholder': 'Enter location of the post'}),
            'description': forms.Textarea(attrs={'class': 'form-control bg-light my-1', 'rows': '5'})

        }
