from django import template
register=template.Library()
from blog.models import *

@register.filter
def make_short(value):
    return value[:100]+'. . .'

@register.inclusion_tag('blog/popularposts.html')
def popular():
    posts=Post.objects.filter(status=1).order_by('-created_date')
    return {'posts':posts}

@register.inclusion_tag('blog/categories.html')
def cat():
    posts=Post.objects.filter(status=1)
    categories=Category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}
    