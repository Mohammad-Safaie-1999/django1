from django.db import models
from django.utils import timezone
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(null=True)
    updated_date=models.DateTimeField(auto_now=True)

    
