from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.views import login

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


class Institutions(View):

    def get(self, request):
        context = {}
        return render(request, 'institutions/institutions.html', context)
