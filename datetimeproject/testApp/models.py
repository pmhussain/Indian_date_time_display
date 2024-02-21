from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    rno = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)