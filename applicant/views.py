from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def index(request):
    context={'testv':'just trying out a few things'}
    return render(request,'applicant/index.html',context)

def register(request):
    context={'apply': forms.Application}
    return render(request, 'applicant/register.html',context)
