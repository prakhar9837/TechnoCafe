from django.urls import path
from . import views

urlpatterns = [
    path('',views.orderSummary, name='orderSummary'),
    path('payment',views.payment, name='payment'),
    path('placed',views.placed, name='placed'),
]