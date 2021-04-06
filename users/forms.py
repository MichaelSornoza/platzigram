from django import forms

from .models import User, Profile


class SignupForm(forms.Form):
    username = forms.CharField(
        label=False,
        min_length=4,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                'required': True
            },
        ),
    )

    password = forms.CharField(
        label=False,
        min_length=8,
        max_length=80,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control',
                'required': True
            },
        ),
    )
    password_confirmation = forms.CharField(
        label=False,
        min_length=8,
        max_length=80,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password Confirmation',
                'class': 'form-control',
                'required': True
            },
        ),
    )
    first_name = forms.CharField(
        label=False,
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'class': 'form-control',
                'required': True
            },
        ),
    )

    last_name = forms.CharField(
        label=False,
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'class': 'form-control',
                'required': True
            },
        ),
    )

    email = forms.CharField(
        label=False,
        min_length=5,
        max_length=70,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control',
                'required': True
            },
        ),
    ),

    def clean_username(self):
        username = self.cleaned_data['username']

        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError('Username is already in use')

        return username

    def clean(self):

        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password do not match')

        return data

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
