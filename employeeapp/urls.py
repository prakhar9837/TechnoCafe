from django.urls import path
from . import views

urlpatterns = [
    path('',views.Elogin, name='Elogin'),
    path('loggedin',views.employee, name='employee'),
    path('AddEmp',views.AddEmp,name='AddEmp'),
    path('AddItem',views.AddItem,name='AddItem'),
    path('AddSup',views.AddSup,name="AddSup"),
    path('AddIngr',views.AddIngr,name="AddIngr"),
    path('AddReqIngr',views.AddReqIngr,name="AddReqIngr"),
]