from django.urls import path
from . import views

urlpatterns = [
   
    path("",views.home,name="home"),
    path("register",views.register,name="register"),
     path("register2",views.getname,name="getname"),
    path('login',views.mylogin,name="mylogin"),
    path('logout',views.mylogout,name="mylogout"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('createrecord',views.createrecord,name="createrecord"),
    path('updaterecord/<int:pk>',views.updateRecord,name="updateRecord"),
    path('viewrecord/<int:pk>',views.viewRecord,name="viewRecord"),
    path('deleterecord/<int:pk>',views.deleteRecord,name="deleteRecord")
]