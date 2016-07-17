from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from django.contrib.auth.views import login
from registration.backends.hmac.views import RegistrationView

from  studentools.forms import (
    SignUpForm,
    LogInForm
)

class Home(View):

    def get(self, request):
        context = {}
        if request.user.is_authenticated():
            return render(request, 'index.html', context)
        else:
            return login(request, authentication_form=LogInForm)

    def post(self, request):
        return login(request, authentication_form=LogInForm)


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
