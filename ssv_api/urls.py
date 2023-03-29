from django.urls import path
 
from . import views,testdb,TopViews

 
urlpatterns = [
    path('User/', testdb.Userdb),
    path('reg/', views.Register),
    path('login/', views.Login),
    path('top/user/', TopViews.Userdb),
    path('top/alarm/', TopViews.Alarmdb),
    path('top/table1/', TopViews.TopTable1),
    path('top/table2/', TopViews.TopTable2),
    path('top/table3/', TopViews.TopTable3),


    path('store/add/', testdb.StoreAdd),
    path('device/add/', testdb.DeviceAdd),
    path('sensor/add/', testdb.SensorAdd),
]