from django.db import models

# Create your models here.
class Post(models.Model):
    caption = models.TextField(max_length=30)
    post_by = models.TextField(max_length=40)
    location = models.TextField(max_length=40)
