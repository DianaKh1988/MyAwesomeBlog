from django.db import models
from django.forms import DateField


class Post(models.Model):
    image = models.ImageField(upload_to='event_images/')
    title = models.CharField(max_length=300)
    text = models.TextField()
    date = models.DateField()

    def get_summary(self):
        return self.text[:40]

    def __str__(self):
        return self.title

