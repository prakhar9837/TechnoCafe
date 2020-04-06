# Generated by Django 2.2.7 on 2019-11-27 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0003_itemrequires'),
        ('supplierapp', '0002_delete_ssupplies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ssupplies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IngrName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeapp.ingredients')),
                ('SupId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplierapp.supplier')),
            ],
        ),
    ]