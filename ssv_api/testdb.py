from django.http import HttpResponse
from django.db import models
from ssvorm.models import  User,Role,Right
# 数据库操作
def Userdb(request):
    list = User.objects.all()
    response = ''
    response1 = "<p>" + '一共有 %s 个用户' % len(list) + "</p>"
    response = response + response1
    for var in list:
        responsetmp = "<p>" + "用户的名字是 %s" % ( var.user_name) + "</p>"
        response = response + responsetmp
    return HttpResponse(response )