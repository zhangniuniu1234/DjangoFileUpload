from django.db import models

# Create your models here.
from tinymce.models import HTMLField


class Student (models.Model):
    s_name=models.CharField(max_length=16)
    s_pic=models.ImageField(upload_to='s_icons/%Y/%m/%d')
    def __str__(self):
        return self.s_name


class Blog(models.Model):
    b_title=models.CharField(max_length=12)
    b_content=HTMLField()
