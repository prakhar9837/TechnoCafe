from django.shortcuts import render, redirect
from supplierapp.models import supplier
from employeeapp.models import ingredients as ingr
# Create your views here.
def Slogin(request):
    if(request.method == 'POST'):
        Sid = request.POST['id']
        password = request.POST['password']
        user = 0
        for obj in (supplier.objects.all()):
            if(obj.SupId == Sid and obj.SupPassword == password):
                user = 1
                break
        print("value of user is :",user)
        if(user):
            return redirect('/supplier/SloggedIn')
        return redirect('/')
    else:
        return render(request,'Slogin.html')

def SloggedIn(request):
    #ingr1 = ingr.objects.all()
    lst = []
    for x in ingr.objects.all():
        v = x.IngrName
        u = x.IngrAmt
        lst.append([v,u])
    return render(request,'SupPage.html',{'dct': lst})