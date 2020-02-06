from django.db import models
from time import strftime


class Ad(models.Model):
    photo = models.FileField(upload_to='pictures/')
    title = models.CharField(max_length=100)
    category = models.TextField(max_length=100)
    about = models.TextField(max_length=1024)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    publish= models.DateTimeField(default=strftime('%Y-%m-%d %H:%M:%S'))

