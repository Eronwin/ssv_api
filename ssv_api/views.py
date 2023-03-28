from django.http import HttpResponse
from ssvorm import models
import json,uuid

# 用户注册
def Register(request):
    if request.method == "POST":
        # 获取前端传来的数据
        json_str = request.body
        json_obj = json.loads(json_str)
        uName = json_obj['user_name']
        uPassword = json_obj['user_password']
        uPhoneNum = json_obj['user_phone_num']
        if models.User.objects.filter(user_name = uName):
            return HttpResponse("<p>用户名已存在！</p>")
        if models.User.objects.filter(user_phone_num = uPhoneNum):
            return HttpResponse("<p>手机号已存在！</p>")
        tUser = models.User(user_id = uuid.uuid1().__str__()[:32], user_name = uName, user_password = uPassword, user_phone_num = uPhoneNum)
        tUser.save()
        if models.User.objects.filter(user_name = uName):
            return HttpResponse("<p>注册成功！</p>")
        else:
            return HttpResponse("<p>注册失败！</p>")
    else:
        return HttpResponse("<p>请求方法错误！</p>")
#登录校验
def Login(request):
    if request.method == "POST":
        json_str = request.body
        json_obj = json.loads(json_str)
        uName = json_obj['user_name']
        uPassword = json_obj['user_password']
        if models.User.objects.filter(user_name = uName, user_password = uPassword):
            return HttpResponse("<p>登录成功！</p>")
        else:
            return HttpResponse("<p>用户名或密码错误！</p>")
