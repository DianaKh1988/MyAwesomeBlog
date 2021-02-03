from django.db import models
from django.forms import DateField


class Blog(models.Model):
    blog_title = models.CharField(max_length=30)
    blog_date = models.DateField(auto_now_add=True)
    blog_text = models.CharField(max_length=500)
    blog_image = models.ImageField(upload_to='blog_images/')

