from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.TextField(max_length=50)
    age = models.DecimalField(max_digits=5, decimal_places=0)