# Generated by Django 2.0 on 2019-05-02 11:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0003_delete_schedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='update',
            old_name='From',
            new_name='From_Engineer',
        ),
        migrations.AlterField(
            model_name='update',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
