from django.shortcuts import render,redirect
from .models import customerclass
from django.contrib import messages,auth
from employeeapp.models import items as ite
from ordersapp.models import orders as ords
import time
# Create your views here.

def customer(request):
    #ords2 = ords(OrderId = 0, ItemId = ite(ItemId = 'i101'), ItemQty = 0)
            #print("orderid",ords2.OrderId) 
    #ords2.save()
    item = ite.objects.all()
    ords1 = ords.objects.all()
    if(request.method == 'POST'):
        val1 = {}
        print("item length",len(item))
        for it5 in item:
            val1[it5.ItemId] = int(request.POST[it5.ItemId])
        print("value of item",it5.ItemId)
        #for i in range(len(item)):
        #val1.append(request.POST['i101'])
        #val1.append(request.POST['i900'])
        print(val1)
        ##i = ords()
        
        for i in ords1:
            k = i.OrderId
        k+=1
        for it in val1 :
            #print("01111")
            #print(it,val1[it])
            if val1[it] != 0:
                ords2 = ords(OrderId = k, ItemId = ite(ItemId = it), ItemQty = val1[it])
                ords2.save()
            #time.sleep(1)
        return redirect('/orders')
        #print(val1)           
    else:    
        #print("hello",len(item))
        return render(request,'customer.html', {'items':item})

def Clogin(request):
    if(request.method == 'POST'):
        username = request.POST['phone']
        password = request.POST['password']
        user = 0
        for obj in (customerclass.objects.all()):
            if(obj.id == username and obj.password == password):
                user = 1
                break
        if(user):
            return redirect('/customer/loggedin')
        return redirect('/')
    else:
        return render(request,'Clogin.html')

def Cregister(request):
    if(request.method == 'POST'):
        phone = request.POST['phone']
        name = request.POST['name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        id1 = int(phone) % 10000
        if(password1 == password2):
            customer = customerclass(id = id1, name=name, phone=phone, password = password1)
            customer.save()
            messages.info(request,'Registration Done')
            print('user created')
            return redirect('Cregister')
        return redirect('/customer/')
    else:
        return render(request,'Cregister.html')