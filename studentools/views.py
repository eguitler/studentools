from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from django.contrib.auth.views import login
from registration.backends.hmac.views import RegistrationView

from studentools.settings import REGISTRATION_OPEN
from studentools.forms import (
    SignUpForm,
    LogInForm
)

class Home(View):

    def get(self, request):
        if os.getenv('MAINTENANCE'):
            return render(request, 'maintenance.html')
        context = {}
        return render(request, 'index.html', context)


class AboutUs(View):

    def get(self, request):
        context = {}
        return render(request, 'about_us.html', context)


class HowWorks(View):

    def get(self, request):
        context = {}
        return render(request, 'how_works.html', context)


class Contact(View):

    def get(self, request):
        context = {}
        return render(request, 'contact.html', context)


class Profile(View):

    def get(self, request):
        context = {}
        return render(request, 'registration/profile.html', context)


class Registration(RegistrationView):

    def get(self, request):
        context = {}
        form = SignUpForm()
        context.update(dict(form=form))
        return render(request, 'registration/registration_form.html', context)

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            self.register(form)
            return render(request, 'registration/registration_complete.html')
        else:
            context = dict(form=form)
            return render(request, 'registration/registration_form.html', context)

    def register(self, form):
        user = super(Registration, self).register(form)


class Institutions(View):

    def get(self, request):
        context = {}
        return render(request, 'institutions/institutions.html', context)
