from django.http import HttpResponse
from ssvorm import models
import json,uuid

# 查看用户信息
def Userdb(request):
    if request.method == "POST":
        # 获取前端传来的数据
        json_str = request.body
        json_obj = json.loads(json_str)
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
        uID = json_obj['user_id']
        tAlarm = models.Alarm.objects.filter(user_alarm_id = uID)
        if tAlarm:
            response = ""
            for i in range(len(tAlarm)):
                response += "<p>第" + str(i + 1) + "条报警信息：</p>"
                response += "<p>报警id：" + str(tAlarm[i].alarm_id) + "</p>"
                response += "<p>报警描述：" + str(tAlarm[i].alarm_desc)+ "</p>"
            return HttpResponse(response)
        else:
            return HttpResponse("<p>报警为空</p>")
    else:
        return HttpResponse("<p>请求方法错误！</p>")

# 门店状态表
def TopTable1(request):
    if request.method == "POST":
        # 获取前端传来的数据
        json_str = request.body
        json_obj = json.loads(json_str)
        uID = json_obj['user_id']
        tStore = models.Store.objects.filter(store_manager_id = uID)
        if tStore:
            response = ""
            status = {0:"正常",1:"警告",2:"危险",3:"待机",4:"未知"}
            statuscnt =[0,0,0,0,0]
            for i in range(len(tStore)):
                response += "<p>第" + str(i + 1) + "条门店信息：</p>"
                response += "<p>门店id：" + str(tStore[i].store_id) + "</p>"
                statuscnt[int(tStore[i].store_status)] += 1
            response += "<p>门店状态统计：</p>"
            for i in range(len(statuscnt)):
                response += "<p>" + status[i] + "：" + str(statuscnt[i]) + "</p>"
            return HttpResponse(response)
        else:
            return HttpResponse("<p>门店为空</p>")
    else:
        return HttpResponse("<p>请求方法错误！</p>")

# 设备状态表
def TopTable2(request):
    if request.method == "POST":
        # 获取前端传来的数据
        json_str = request.body
        json_obj = json.loads(json_str)
        uID = json_obj['user_id']
        tStore = models.Store.objects.filter(store_manager_id = uID)
        if tStore:
            response = ""
            status = {0:"运行",1:"故障",2:"停用"}
            statuscnt =[0,0,0]
            for i in range(len(tStore)):
                tDevice = models.Device.objects.filter(device_store_id = tStore[i].store_id)
                if tDevice:
                    for j in range(len(tDevice)):
                        response += "<p>第" + str(i + 1) + "个门店的第" + str(j + 1) + "个设备信息：</p>"
                        response += "<p>设备id：" + str(tDevice[j].device_id) + "</p>"
                        response += "<p>设备状态：" + status[int(tDevice[j].device_status)] + "</p>"
                        statuscnt[int(tDevice[j].device_status)] += 1
            response += "<p>设备状态统计：</p>"
            for i in range(len(statuscnt)):
                response += "<p>" + status[i] + "：" + str(statuscnt[i]) + "</p>"
            return HttpResponse(response)
        else:
            return HttpResponse("<p>设备为空</p>")

#传感器信息表:

def TopTable3(request):
    if request.method == "POST":
        # 获取前端传来的数据
        json_str = request.body
        json_obj = json.loads(json_str)
        uID = json_obj['user_id']
        tStore = models.Store.objects.filter(store_manager_id = uID)
        if tStore:
            response = ""
            status = {0:"正常",1:"警告",2:"危险",3:"故障"}
            statuscnt =[0,0,0,0]
            for i in range(len(tStore)):
                tDevice = models.Device.objects.filter(device_store_id = tStore[i].store_id)
                if tDevice:
                    for j in range(len(tDevice)):
                        tSensor = models.Sensor.objects.filter(sensor_device_id = tDevice[j].device_id)
                        if tSensor:
                            for k in range(len(tSensor)):
                                response += "<p>第" + str(i + 1) + "个门店的第" + str(j + 1) + "个设备的第" + str(k + 1) + "个传感器信息：</p>"
                                response += "<p>传感器id：" + str(tSensor[k].sensor_id) + "</p>"
                                response += "<p>传感器状态：" + status[int(tSensor[k].sensor_status)] + "</p>"
                                statuscnt[int(tSensor[k].sensor_status)] += 1
            response += "<p>传感器状态统计：</p>"
            for i in range(len(statuscnt)):
                response += "<p>" + status[i] + "：" + str(statuscnt[i]) + "</p>"
            return HttpResponse(response)
        else:
            return HttpResponse("<p>传感器为空</p>")