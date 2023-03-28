from django.urls import path
 
from . import views,testdb,TopViews

 
urlpatterns = [
    path('User/', testdb.Userdb),
    path('reg/', views.Register),
    path('login/', views.Login),
    path('top/user/', TopViews.Userdb),
]