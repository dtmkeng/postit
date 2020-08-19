from django.db import models

# Create your models here.
class Gender(models.Model):
    gender =  models.CharField(max_length=60)
    
    def __str__(self):
        return self.gender

class Student(models.Model):
    name = models.TextField(max_length=50)
    age = models.DecimalField(max_digits=5, decimal_places=0)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

