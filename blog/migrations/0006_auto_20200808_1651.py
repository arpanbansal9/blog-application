# Generated by Django 3.0.5 on 2020-08-09 00:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200808_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addblog',
            name='slug',
        ),
        migrations.AlterField(
            model_name='addblog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 8, 16, 51, 36, 782527)),
        ),
    ]
