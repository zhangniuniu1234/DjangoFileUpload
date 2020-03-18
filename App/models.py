from django.db import models

# Create your models here.

class Student (models.Model):
    s_name=models.CharField(max_length=16)
    s_pic=models.ImageField(upload_to='s_icons')
