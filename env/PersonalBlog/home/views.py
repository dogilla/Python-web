from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views import View

# Create your views here.

def index(View):
    return render(request,'index.html')


class Index(View):
    template = 'home/index.html'
    context = {'title':'Index'}

    def get(self, request):
        return render(request, self.template, self.context)

class About(View):
    template = 'home/about.html'
    context = {'title': 'About me'}
    def get(self, request):
        return render(request, self.template, self.context )

