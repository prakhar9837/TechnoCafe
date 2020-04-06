from django.db import models
from employeeapp.models import employee as emp
from employeeapp.models import ingredients as ingr
# Create your models here.
class supplier(models.Model):
    SupId = models.CharField(max_length=20, primary_key=True)
    SupName = models.CharField(max_length=50)
    SupPassword = models.CharField(max_length=50)
    SupPh = models.CharField(max_length=15)
    EmpId = models.ForeignKey(emp,on_delete = models.DO_NOTHING)

class Ssupplies(models.Model):
    SupId = models.ForeignKey(supplier, on_delete=models.CASCADE)
    IngrName = models.ForeignKey(ingr, on_delete=models.CASCADE)
    class meta:
        unique_together = ('SupId','IngrName')

