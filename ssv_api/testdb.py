from django.http import HttpResponse
from django.db import models
from ssvorm.models import  User,Role,Right,Store,Device,Sensor

import json,uuid,random
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

def StoreAdd(request):
    if request.method == "POST":
        # 获取前端传来的数据
        json_str = request.body
        json_obj = json.loads(json_str)
        uID = json_obj['user_id']
        for i in range(100):
            tStore = Store(store_id = uuid.uuid1().__str__()[:32], store_name = "测试门店" + str(i), store_address = "测试地址" + str(i), store_address_code = "测试地址解码" + str(i), store_phone_num = "测试电话" + str(i), store_manager_id = uID,store_status = random.randint(0,4))
            tStore.save()
        if Store.objects.filter(store_manager_id = uID):
            return HttpResponse("<p>注册成功！</p>")
        else:
            return HttpResponse("<p>注册失败！</p>")
    else:
        return HttpResponse("<p>请求方法错误！</p>")

def DeviceAdd(request):
    if request.method == "POST":
        # 获取前端传来的数据
        json_str = request.body
        json_obj = json.loads(json_str)
        uID = json_obj['user_id']
        tStore = Store.objects.filter(store_manager_id = uID)
        for i in range(1000):
            tDevice = Device(device_id = uuid.uuid1().__str__()[:32], device_name = "测试设备" + str(i), device_type = "测试设备类型" + str(i),  device_store_id = random.choice(tStore).store_id,device_status = random.randint(0,2))
            tDevice.save()
        if Device.objects.filter(device_manager_id = uID):
            return HttpResponse("<p>注册成功！</p>")
        else:
            return HttpResponse("<p>注册失败！</p>")
    else:
        return HttpResponse("<p>请求方法错误！</p>")

def SensorAdd(request):
    if request.method == "POST":
        # 获取前端传来的数据
        json_str = request.body
        json_obj = json.loads(json_str)
        uID = json_obj['user_id']
        tStore = Store.objects.filter(store_manager_id = uID)
        for i in range(10000):
            tDevice = Device.objects.filter(device_store_id = random.choice(tStore).store_id)
            tSensor = Sensor(sensor_id = uuid.uuid1().__str__()[:32], sensor_name = "测试传感器" + str(i), sensor_type = "测试传感器类型" + str(i),  sensor_device_id = random.choice(tDevice).device_id,sensor_status = random.randint(0,3),sensor_value = random.randint(0,100))
            tSensor.save()
        if Sensor.objects.filter(sensor_manager_id = uID):
            return HttpResponse("<p>注册成功！</p>")
        else:
            return HttpResponse("<p>注册失败！</p>")
    else:
        return HttpResponse("<p>请求方法错误！</p>")