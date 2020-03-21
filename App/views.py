import os
import random

from PIL import Image,ImageDraw,ImageFont
from django.http import HttpResponse
from django.shortcuts import render
import io

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


def get_vertify_code(request):
    image_background=(255,0,0)
    #构造画布
    image=Image.new("RGB",(100,50),image_background)
    #画笔
    draw=ImageDraw.Draw(image,'RGB')

    #改变字体和大小
    # imagefont=ImageFont.truetype("path",30)
    # 绘制
    # draw.text((20, 10), "hello", font=imagefont)
    vertify_code = ''

    imagefont=ImageFont.truetype(os.path.join(BASE_DIR,'static/SpaceMono-Bold.ttf'),size=30,)

    vertify_str="abcdefghigklmnopqrstuvwxyzQWERTYUIOPLKMJNHBGVFCDXSZA1234567890"
    for i in  range(4):
        char=random.choice(vertify_str)
        vertify_code+=char
        x=random.randrange(15)+25*i
        draw.text((x,random.randrange(20)),char,fill=get_color(),font=imagefont)

    for i in range(500):
        draw.point((random.randrange(100),random.randrange(50)),fill=get_color())

    request.session['vertify_code']=vertify_code


    #缓冲
    buffer=io.BytesIO()
    image.save(buffer,"png")
    #注意写类型
    return HttpResponse(buffer.getvalue(),content_type="image/png")

def get_color():
    red=random.randrange(256)
    green=random.randrange(256)
    blue=random.randrange(256)
    return red,green,blue

def login(request):
    if request.method=='GET':
        return render(request, 'login.html')
    elif request.method=='POST':
        vertify_code=request.POST.get("vertify_code")
        username=request.POST.get("username")
        vertify_code_source=request.session.get("vertify_code")
        if vertify_code!=vertify_code_source:
            return HttpResponse("验证码错误")
        return HttpResponse("登陆成功")


def blog_editor(request):
    if request.method=='GET':
        return render(request, 'BlogEditor.html')
    elif request.method=='POST':
        print(request.POST.get("content"))
        return HttpResponse("提交成功")

