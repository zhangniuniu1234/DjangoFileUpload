from django.conf.urls import url, include
from django.contrib import admin
from App import  views

urlpatterns = [
    url(r'^upload/',views.UploadView.as_view(),name='upload'),
    url(r'^geticon/', views.get_icon),
    url(r'^getvertifycode/',views.get_vertify_code,name='get_vertify_code'),
    url(r'^login/',views.login),
    url(r'^blogeditor/', views.blog_editor)

]