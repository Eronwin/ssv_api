from django.http import HttpResponse
from ssvorm import models
import json,uuid

# 查看用户信息
def Userdb(request):
    if request.method == "POST":
        # 获取前端传来的数据
        json_str = request.body
        json_obj = json.loads(json_str)
        print(json_obj)
        uID = json_obj['user_id']
        tUser = models.User.objects.filter(user_id = uID)
        if tUser:
            response = "<p>用户id：" + tUser[0].user_id + "</p>"
            response += "<p>用户名：" + tUser[0].user_name + "</p>"
            response += "<p>用户密码：" + tUser[0].user_password + "</p>"
            response += "<p>用户手机号：" + tUser[0].user_phone_num + "</p>"
            response += "<p>用户性别：" + tUser[0].user_sex + "</p>"
            response += "<p>用户地址：" + tUser[0].user_location + "</p>"
            response += "<p>用户联系地址：" + tUser[0].user_contact_address + "</p>"
            response += "<p>用户联系地址解码：" + tUser[0].user_contact_address_code+ "</p>"
            return HttpResponse(response)
        else:
            return HttpResponse("<p>用户信息查询失败！</p>")
    else:
        return HttpResponse("<p>请求方法错误！</p>")
# 所属报警信息
def Alarmdb(request):
    if request.method == "POST":
        # 获取前端传来的数据
        json_str = request.body
        json_obj = json.loads(json_str)
        print(json_obj)
        uID = json_obj['user_id']
        tAlarm = models.Alarm.objects.filter(user_id = uID)
        if tAlarm:
            response = "<p>报警id：" + tAlarm[0].alarm_id + "</p>"
            response += "<p>报警时间：" + tAlarm[0].alarm_time + "</p>"
            response += "<p>报警类型：" + tAlarm[0].alarm_type + "</p>"
            response += "<p>报警状态：" + tAlarm[0].alarm_state + "</p>"
            response += "<p>报警描述：" + tAlarm[0].alarm_description + "</p>"
            response += "<p>报警图片：" + tAlarm[0].alarm_picture + "</p>"
            response += "<p>报警视频：" + tAlarm[0].alarm_video + "</p>"
            response += "<p>报警用户id：" + tAlarm[0].user_id + "</p>"
            return HttpResponse(response)
        else:
            return HttpResponse("<p>报警信息查询失败！</p>")
    else:
        return HttpResponse("<p>请求方法错误！</p>")