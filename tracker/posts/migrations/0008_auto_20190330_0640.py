# Generated by Django 2.0 on 2019-03-30 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20190330_0351'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Week',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
