from django.contrib import admin

# Register your models here.

from Two.models import Gamer, Grade, student


class GamerAdmin(admin.ModelAdmin):

    def get_sex(self):
        if self.g_sex:
            return "男"
        elif self.g_sex==False:
            return "女"
        else:
            return "保密"

    get_sex.short_description = "性别"

    list_display = ("g_name","g_age",get_sex)
    search_fields = ["g_name"]
    list_filter = ['g_sex',"g_age"]
    fieldsets = (
        ("基本信息",{"fields":["g_name","g_age","g_sex"]}),
        ("会员信息", {"fields":["g_vip"]}),
    )

admin.site.register(Gamer,GamerAdmin)


#插入一个班级的同时插入两个学生
class StudentInfo(admin.TabularInline):
    model = student
    extra = 3

class GradeAdmin(admin.ModelAdmin):
    inlines = [StudentInfo]


#注册
admin.site.register(Grade,GradeAdmin)
admin.site.register(student)

class TeachSite(admin.AdminSite):
    site_title = 'hello'
    site_header = '张妞妞'
    site_url = '/two/index'

site=TeachSite()
site.register(Grade,GradeAdmin)
site.register(student)
