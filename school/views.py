from django.shortcuts import render

# Create your views here.

def index(request):
    context={'tests':'this is my home page'}
    return render(request,'school/index.html',context)
