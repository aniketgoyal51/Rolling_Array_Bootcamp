from django.db import models
from datetime import datetime

# Create your models here.
class Blogs (models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=5000000)
    time=models.DateTimeField(default=datetime.now,blank=True)