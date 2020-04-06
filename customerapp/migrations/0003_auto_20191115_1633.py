# Generated by Django 2.2.7 on 2019-11-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0002_customerclass_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerclass',
            old_name='price',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='customerclass',
            name='desc',
        ),
        migrations.AddField(
            model_name='customerclass',
            name='password',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]