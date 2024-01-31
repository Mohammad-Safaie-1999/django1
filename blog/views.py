from django.shortcuts import render

def index_home_blog (request):
    return render (request,'blog/blog-home.html')

def index_single (request):
    return render (request,'blog/blog-single.html')

