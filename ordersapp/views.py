from django.shortcuts import render,redirect
from employeeapp.models import items as ite
from ordersapp.models import orders
import time
# Create your views here.
 
def orderSummary(request):
    ords1 = orders.objects.all()
    item = ite.objects.all()
    lst = []
    for i in ords1:
        lats = i.OrderId
    v = ""
    u=0
    sum1=0
    for x in ords1:
        if x.OrderId == lats:
            for z in item:
                if x.ItemId.ItemId == z.ItemId:
                    v = z.ItemName
                    u = z.ItemPrice
                    sum1 += u*x.ItemQty
            lst.append([v,x.ItemQty,u])
    cgst = 0.025 * sum1
    total = 2*cgst + sum1
    print(lst)
    return render(request,'orderSum.html',{'dct':lst , 'sum1':sum1, 'cgst':cgst, 'total':total})

def payment(request):
    return render(request,'payment.html')

def placed(request):
    time.sleep(2)
    return render(request,'placed.html')