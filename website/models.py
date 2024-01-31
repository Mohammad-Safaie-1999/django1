from django.db import models
from django.utils import timezone

class Contact (models.Model):
    name=models.CharField(max_length=25)
    subject=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    updated_date=models.DateTimeField(auto_now=True)


