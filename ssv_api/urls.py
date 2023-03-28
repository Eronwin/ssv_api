from django.urls import path
 
from . import views,testdb
 
urlpatterns = [
    path('a/', views.hello),
    path('b/', testdb.testdb),
]