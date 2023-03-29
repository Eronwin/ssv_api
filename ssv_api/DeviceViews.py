from django.http import HttpResponse
from ssvorm import models
import json,uuid


#用户门店列表
def Storedb(request):
    if request.method == "POST":
        # 获取前端传来的数据
        json_str = request.body
        json_obj = json.loads(json_str)
        uID = json_obj['user_id']
        tStore = models.Store.objects.filter(store_manager_id = uID)
        if tStore:
            response = ""
            for i in range(len(tStore)):
                response += "<p>第" + str(i + 1) + "条门店信息：</p>"
                response += "<p>门店id：" + str(tStore[i].store_id) + "</p>"
                response += "<p>门店名称：" + str(tStore[i].store_name) + "</p>"
                response += "<p>门店地址：" + str(tStore[i].store_address) + "</p>"
                response += "<p>门店地址解码：" + str(tStore[i].store_address_code) + "</p>"
                response += "<p>门店联系电话：" + str(tStore[i].store_phone_num) + "</p>"
            return HttpResponse(response)
        else:
            return HttpResponse("<p>门店为空</p>")
    else:
        return HttpResponse("<p>请求方法错误！</p>")