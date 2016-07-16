from django import forms

from django.contrib.auth.forms import AuthenticationForm

class LogInForm(AuthenticationForm):
    username = forms.CharField(min_length=6, strip=True, label='', widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(min_length=6, label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))


class SignUpForm(forms.Form):
    username = forms.CharField(min_length=6, strip=True)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)
    repassword = forms.CharField(min_length=6, widget=forms.PasswordInput)