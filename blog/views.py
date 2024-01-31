from django.shortcuts import render,get_object_or_404
from blog.models import Post



def index_home_blog (request):
    posts=Post.objects.filter(status=1)
    context={'posts':posts}
    return render (request,'blog/blog-home.html',context)

def index_single (request,pid):
    post=get_object_or_404(Post,id=pid)
    context={'post':post}
    return render (request,'blog/blog-single.html',context)



