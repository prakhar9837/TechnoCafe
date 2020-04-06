from django.db import models

# Create your models here.
class employee(models.Model):
    EmpId = models.CharField(max_length=20, primary_key=True)
    EmpName = models.CharField(max_length=50)
    EmpPassword = models.CharField(max_length=50)
    EmpPh = models.CharField(max_length=15)
    EmpCategory = models.CharField(max_length=20)

class items(models.Model):
    ItemId = models.CharField(max_length=20, primary_key=True)
    ItemCategory = models.CharField(max_length=50)
    ItemName = models.CharField(max_length=20)
    ItemPrice = models.IntegerField()
    ItemDesc = models.CharField(max_length=200)
    EmpId = models.ForeignKey('employee', on_delete = models.DO_NOTHING)

class ingredients(models.Model):
    IngrName = models.CharField(max_length=50, primary_key=True)
    IngrAmt = models.IntegerField()


class itemRequires(models.Model):
    ItemId = models.ForeignKey('items', on_delete=models.CASCADE)
    IngrName = models.ForeignKey('ingredients', on_delete=models.CASCADE)
    ItemQty = models.IntegerField()
    class meta:
        unique_together = ('ItemId','IngrName')
    