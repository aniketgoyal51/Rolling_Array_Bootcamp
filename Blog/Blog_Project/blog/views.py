from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Blogs

# Create your views here.

def index(request):
    blog=Blogs.objects.all()
    print(Blogs.objects.all())
    return render(request,'index.html',{"blogs":blog})


def postBlog(request):
    if(request.method=="POST"):
        title=request.POST['title']
        body=request.POST['body']

        blog=Blogs.objects.create(title=title,body=body)
        blog.save()
        messages.success(request, "Blog posted successfully!")
        return redirect("/")
    else:
        return render(request,'postBlog.html')


def post(request,blog):
    post=Blogs.objects.get(id=blog)
    print(post)
    return render(request,'post.html',{"blog":post})