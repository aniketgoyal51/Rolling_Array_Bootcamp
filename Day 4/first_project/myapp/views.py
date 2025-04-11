from django.shortcuts import render
from django.http import HttpResponse
from .models import Features

# Create your views here.

def index(request):
    context={'name':"Aniket","age":"19"}
    return render(request,'index.html',context)

def counter(request):
    feature=Features.objects.all()
    return render(request,'counter.html',{'feature':feature})