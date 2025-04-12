from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Register

# Create your views here.
def index(request):
    names=["Aniket","nitin","dhruv","sid","gauri"]
    return render(request,'index.html',{"names":names})


def register(request):
    print(request)
    if(request.method=='POST'):
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        print(request)

        if(password==password2):
            if(Register.objects.filter(email=email).exists()):
                messages.info(request,"email already exists")
                return redirect('register')
            if(Register.objects.filter(name=name).exists()):
                messages.info(request,"name already used")
                return redirect('register')
            else:
                user=User.objects.create_user(username=name,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"password doesn's match")
            return redirect('register')
    else:
        return render(request,'registration.html')


def login(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        
        user= auth.authenticate(username=username,password=password)

        if(user is not None):
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Cridentials are wrong")
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request,pk):
    return render(request,'post.html',{'pk':pk})