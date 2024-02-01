from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to='blog/',default='blog/default.jpg')
    title=models.CharField(max_length=100)
    content=models.TextField()
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    category=models.ManyToManyField(Category)
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(null=True)
    updated_date=models.DateTimeField(auto_now=True)

    
