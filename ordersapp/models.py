from django.db import models
from customerapp.models import customerclass as cust
from employeeapp.models import items as item
# Create your models here.

class orders(models.Model):
    OrderId = models.IntegerField()
    ItemId = models.ForeignKey(item, on_delete = models.DO_NOTHING)
    ItemQty = models.IntegerField()
    class meta:
        unique_together = ('OrderId','ItemId')
    
class payment(models.Model):
    PayId = models.CharField(max_length=20, primary_key=True)
    PayMode = models.CharField(max_length=50)
    PayAmt = models.IntegerField()
    