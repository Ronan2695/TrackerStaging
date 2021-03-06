# Generated by Django 2.0 on 2019-05-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20190426_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Mode_of_Alert',
            field=models.TextField(db_column='mode', default='Manual Check'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Month',
            field=models.CharField(db_column='menth', default='May', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='Responded_Time',
            field=models.CharField(db_column='rtime', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Shift',
            field=models.TextField(db_column='shyft', default='emea'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Time_spent',
            field=models.CharField(db_column='wtime', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Week',
            field=models.IntegerField(db_column='weekno', default=18, null=True),
        ),
    ]
