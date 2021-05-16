from django import forms
from django.contrib.auth import get_user_model
import re

User = get_user_model()


class contactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your Full Name"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "enter your Email Address"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "enter your Message"})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if not (re.search(email_regex, email)):
            raise forms.ValidationError("Please Enter Email Valid.")
        return email


class loginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "enter your password"})
    )


class registerForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your username"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "enter your email"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "enter your password"})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "enter your password again"})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username has exists")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        qs = User.objects.filter(email=email)
        if not (re.search(email_regex, email)):
            raise forms.ValidationError("Please Enter Email Valid.")
        elif qs.exists():
            raise forms.ValidationError("email has exists")
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise forms.ValidationError("password must match")
        return data
