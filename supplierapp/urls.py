from django.urls import path
from . import views

urlpatterns = [
    path('',views.Slogin, name='Slogin'),
    path('SloggedIn',views.SloggedIn, name='SloggedIn'),
]