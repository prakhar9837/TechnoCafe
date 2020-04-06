from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from employeeapp.models import employee as emp, items as ite, ingredients as ingr, itemRequires as ItRe
from supplierapp.models import supplier
# Create your views here.
def Elogin(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if(user is not None):
            auth.login(request, user)
            return redirect("/employee/loggedin")
        user = 0
        for obj in (emp.objects.all()):
            if(obj.EmpId == username and obj.EmpPassword == password):
                user = 1
                break
        if(user):
            return redirect('/employee/loggedin')
        return redirect('/')
    else:
        return render(request,'Elogin.html')

def employee(request):
    return render(request,'employee.html')

def AddEmp(request):
    if(request.method == 'POST'):
        Category = request.POST['category']
        Id = request.POST['id']
        Name = request.POST['name']
        Ph = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if(password1 == password2):
            emp1 = emp(EmpId = Id, EmpName = Name, EmpPassword = password1, EmpPh=Ph, EmpCategory = Category)
            emp1.save()
            return redirect('/employee/loggedin')
        return redirect('/employee/AddEmp')
    else:
        return render(request,'AddEmp.html')

def AddItem(request):
    if(request.method == 'POST'):
        Id = request.POST['id']
        Category = request.POST['category']
        Name = request.POST['name']
        Price = int(request.POST['price'])
        eid = request.POST['empid']
        desc = request.POST['desc']
        item1 = ite(ItemId = Id, ItemName = Name, ItemCategory = Category, ItemPrice = Price, ItemDesc = desc)
        item1.EmpId = emp(EmpId = eid)
        item1.save()
        messages.info(request,'Item added')
        print('item added')
        return redirect('/employee/AddReqIngr')
    else:
        return render(request,'AddItem.html')

def AddSup(request):
    if(request.method == 'POST'):
        Id = request.POST['id']
        Name = request.POST['name']
        Ph = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        EmpId = request.POST['empId']
        if(password1 == password2):
            sup1 = supplier(SupId = Id, SupName = Name, SupPassword = password1, SupPh=Ph, EmpId = emp(EmpId=EmpId))
            sup1.save()
            messages.info(request,'Supplier added')
            print('supplier added')
            return redirect('/employee/loggedin')
        return redirect('/employee/AddEmp')
    else:
        return render(request,'AddSup.html')

def AddIngr(request):
    if(request.method == 'POST'):
        Name = request.POST['name']
        Amount = int(request.POST['amount'])
        ing1 = ingr(IngrName = Name, IngrAmt = Amount)
        ing1.save()
        messages.info(request,'Ingredient added')
        print('Ingredient added')
        return redirect('/employee/loggedin')
    else:
        return render(request,'AddIngr.html')

def AddReqIngr(request):
    if(request.method == 'POST'):
        Id = request.POST['id']
        Name = request.POST['name']
        Amount = int(request.POST['amount'])
        ingr1 = ItRe(ItemQty = Amount)
        ingr1.ItemId = ite(ItemId = Id)
        ingr1.IngrName = ingr(IngrName = Name)
        ingr1.save()
        messages.info(request,'Ingredient added')
        print('Ingredient added')
        return redirect('/employee/loggedin')
    else:
        return render(request,'AddReqIngr.html')
