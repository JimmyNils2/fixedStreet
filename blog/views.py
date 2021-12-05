from django.shortcuts import render
from .models import Category, Post

# Create your views here.

def blog(request):

    categories=Category.objects.all()
    posts=Post.objects.all()

    return(render(request,'blog/blog.html',{'posts':posts,'categories':categories}))

def category(request,category_id):
    
    category=Category.objects.get(id=category_id)
    
    posts=Post.objects.filter(categories=category)

    return(render(request,'blog/filtered_blog.html',{'category':category,'posts':posts}))
