from django.contrib import admin
from .models import Student, Gender


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'gender',
    )
    
@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = (
        'gender',
    )