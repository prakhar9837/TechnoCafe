# Generated by Django 2.2.7 on 2019-11-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0003_auto_20191115_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerclass',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]