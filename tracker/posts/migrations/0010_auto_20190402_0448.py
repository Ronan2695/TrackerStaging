# Generated by Django 2.0 on 2019-04-02 04:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20190402_0338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Time',
        ),
        migrations.AddField(
            model_name='post',
            name='Complexity',
            field=models.TextField(blank=True, db_column='cmplx', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Interval',
            field=models.IntegerField(blank=True, db_column='intrval', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Start_Time',
            field=models.TimeField(db_column='stime', default='01:00'),
        ),
        migrations.AddField(
            model_name='post',
            name='Ticket_Number',
            field=models.IntegerField(db_column='tkno', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Comments',
            field=models.TextField(db_column='comments', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Date',
            field=models.DateField(db_column='dete', default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Day_Of_Week',
            field=models.TextField(db_column='dayofweek'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Description',
            field=models.TextField(db_column='descrp', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Environment',
            field=models.CharField(db_column='env', default='Please select', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Escalated',
            field=models.CharField(db_column='escalated', default='No', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='Escalated_Reason',
            field=models.CharField(blank=True, db_column='escreason', default='Please select', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Escalated_to',
            field=models.CharField(db_column='escalatedto', default='NA', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='False_Alarm',
            field=models.TextField(db_column='falsealarm'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Host_Name',
            field=models.CharField(db_column='hostname', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Host_Type',
            field=models.CharField(db_column='hostype', default='Please select', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='If_Others_Please_Specify',
            field=models.CharField(db_column='others', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='Incident_Type',
            field=models.CharField(db_column='itype', default='Please select', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Mode_of_Alert',
            field=models.TextField(db_column='mode', default='Manual check'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Month',
            field=models.CharField(db_column='menth', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='NOC_Engineer',
            field=models.CharField(db_column='engineer', default='Please select', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Name',
            field=models.CharField(db_column='name', default='Please select', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Priority',
            field=models.TextField(db_column='priority'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Remediation',
            field=models.TextField(db_column='remediation', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Resolution',
            field=models.TextField(db_column='resolution', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Resolved_by_Engineer',
            field=models.CharField(db_column='resolvedby', default='noc', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='Resolved_by_Team',
            field=models.CharField(db_column='resolvedteam', default='Please select', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Responded_Time',
            field=models.TimeField(db_column='rtime', default='01:00'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Responsible_Team',
            field=models.CharField(db_column='respteam', default='Please select', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Shift',
            field=models.TextField(db_column='shyft'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Source_of_Alert',
            field=models.CharField(db_column='source', default='Please select', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Status',
            field=models.CharField(blank=True, db_column='status', default='Resolved', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Time_spent',
            field=models.TimeField(db_column='wtime'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Week',
            field=models.IntegerField(db_column='weekno', null=True),
        ),
    ]
