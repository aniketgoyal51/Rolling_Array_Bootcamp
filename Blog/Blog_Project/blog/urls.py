from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('postBlog',views.postBlog,name="postBlog"),
    path('post/<str:blog>',views.post,name="post"),
]