from datetime import datetime

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from registration.forms import RegistrationForm
#from registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.models import User

from studentools.models import CustomUser


year = datetime.now().year
BIRTH_YEARS = sorted(range(year-100, year+1), reverse=True)

CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

def ph_email(msg):
    return forms.EmailInput(attrs={'placeholder': msg}) 

def ph_pass(msg):
    return forms.PasswordInput(attrs={'placeholder': msg})

def ph_text(msg):
    return forms.TextInput(attrs={'placeholder': msg})

def set_placeholders(form):
    for field in form.fields.values():
        field.required = True
        if field.label:
            field.widget.attrs['placeholder'] = field.label
        else:
            field.widget.attrs['placeholder'] = field.help_text.capitalize()

class LogInForm(AuthenticationForm):

    class Meta():
        model = CustomUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LogInForm, self).__init__(*args, **kwargs)
        set_placeholders(self)

# In production must have unique email
#class SignUpForm(RegistrationFormUniqueEmail):
class SignUpForm(RegistrationForm):

    class Meta():
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        set_placeholders(self)

    birthday = forms.DateField(required=True, widget=forms.widgets.SelectDateWidget(years=BIRTH_YEARS))
    genere = forms.ChoiceField(required=True, label='', choices=CHOICES, widget=forms.RadioSelect)
