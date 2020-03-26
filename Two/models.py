from django.db import models

# Create your models here.

class Games(models.Model):
    g_name=models.CharField(max_length=32)
    g_price=models.IntegerField(default=0)
    g_desc=models.TextField()
    g_is_public_testing=models.BooleanField(default=False)
    g_public_testing_time=models.DateTimeField(auto_now=True)

class Gamer(models.Model):
    g_name=models.CharField(max_length=32,verbose_name="姓名")
    g_age=models.IntegerField(default=18,verbose_name="年龄")
    #False代表女，True代表男
    g_sex=models.NullBooleanField(default=False,verbose_name="性别")
    g_vip=models.IntegerField(default=0)


class Grade(models.Model):
    g_name=models.CharField(max_length=32,verbose_name='班级名称')
    def __str__(self):
        return self.g_name

class student(models.Model):
    s_name=models.CharField(max_length=32,verbose_name="学生姓名")
    s_grade=models.ForeignKey(Grade)
    def __str__(self):
        return self.s_name