from django.contrib import admin

# Register your models here.
from App.models import Student


#自定义管理类
class StudentAdmin(admin.ModelAdmin):
    pass
#注册学生的时候添加自定义的管理
admin.site.register(Student,StudentAdmin)