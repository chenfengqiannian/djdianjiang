from dianjiang import settings
"""dianjiang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import dianjiangapp

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^userapi/','dianjiangapp.views.userinapi'),
    url(r'^imageupapi/','dianjiangapp.views.imageup'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^gongchengapi/','dianjiangapp.views.gongchengapi'),
    url(r'^shezhiapi/','dianjiangapp.views.shezhiapi'),
    url(r'^signapi/','dianjiangapp.views.signapi'),
    url(r'^zhifubaosignapi/','dianjiangapp.views.zhifubaosignapi'),
    url(r'^weixinsignapi/','dianjiangapp.views.weixinsignapi')
    
    
,url(r'^wanchengimage/','dianjiangapp.views.ImageUpApi')
]
