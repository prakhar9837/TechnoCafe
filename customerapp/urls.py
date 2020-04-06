from django.urls import path
from . import views

urlpatterns = [
    path('',views.Clogin, name='Clogin'),
    path('loggedin',views.customer, name='customer'),
    path('register/',views.Cregister, name='Cregister'),
]