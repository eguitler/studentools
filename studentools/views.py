from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class Home(View):

    def get(self, request):
        context = {}
        return render(request, 'index.html', context)


class Institutions(View):

    def get(self, request):
        context = {}
        return render(request, 'institutions/institutions.html', context)
