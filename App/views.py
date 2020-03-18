import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from App.models import Student
from DjangoDay7.settings import BASE_DIR, MEDIA_URL_PREFIX


class UploadView(TemplateView):
    template_name = 'upload_pic.html'
    def post(self,request):
        icon=request.FILES.get("icon")
        # icons_path=os.path.join(BASE_DIR,'static/icons/%s'%icon.name)
        # with open(icons_path,"wb") as icon_save:
        #     for part in icon.chunks():
        #         icon_save.write(part)
        #         icon_save.flush()
        # print(request.FILES)

        #用model
        username=request.POST.get("username")
        student=Student()
        student.s_name=username
        student.s_pic=icon
        student.save()
        return HttpResponse("上传成功")

def get_icon(request):
    student=Student.objects.last()
    print(student.s_pic)
    print(student.s_pic.path)
    print(MEDIA_URL_PREFIX+student.s_pic.url)
    print(student.s_pic.size)
    return render(request,'image_show.html',context={"image_url":MEDIA_URL_PREFIX+student.s_pic.url})




