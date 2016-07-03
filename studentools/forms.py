from django import forms

class SignUpForm(forms.Form):
	username = forms.CharField(min_length=6, strip=True)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)
    repassword = forms.CharField(min_length=6, widget=forms.PasswordInput)