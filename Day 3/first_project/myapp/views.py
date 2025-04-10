from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context={'name':"Aniket","age":"19"}
    return render(request,'index.html',context)

def counter(request):
    words=request.POST['words']
    count=len(words.split())
    return render(request,'counter.html',{'words':words,'count':count})