from django.db import models
import datetime
from django.utils.translation import gettext as _
from datetime import date
# Create your models here.
class Post(models.Model):
    today = datetime.date.today()
    years = today.year
    Year = models.PositiveSmallIntegerField(blank=False, null=False, db_column='yeer',default=years)

    weeknumber = date.today().isocalendar()[1]
    Week = models.IntegerField(blank=False, null=True, db_column='weekno',default=weeknumber)


    Month = models.CharField(max_length=100, null=False, blank=False, db_column='menth')
    Date = models.DateField(_("Date"), default=datetime.date.today, null=False, blank=False, db_column='dete')
    #Date = models.DateField(widget=forms.AdminDateWidget)
    Shift = models.TextField(null=False, db_column='shyft')
    Day_Of_Week = models.TextField(null=False, db_column='dayofweek')
    Start_Time = models.CharField(max_length=8,blank=False, default='01:00',db_column='stime')
    Responded_Time =  models.CharField(max_length=8,blank=False,default='01:00',db_column='rtime')
    Time_spent = models.CharField(max_length=8,blank=False, db_column='wtime')
    Responsible_Team = models.CharField(max_length=100, null=True, blank=False, default='Please select', db_column='respteam')
    False_Alarm = models.TextField(null=False, db_column='falsealarm')
    Incident_Type = models.CharField(max_length=100, null=True, blank=False, default='Please select', db_column='itype')
    Priority = models.CharField(max_length=10 ,null=False, db_column='priority')
    Name = models.CharField(max_length=100, null=True, blank=False, default='Please select', db_column='name')
    If_Others_Please_Specify = models.CharField(max_length=100,null=False, db_column='others')
    Description = models.TextField(null=True, blank=False, db_column='descrp')
    Environment = models.CharField(max_length=100, null=True, blank=False, default='Please select', db_column='env')
    Host_Type = models.CharField(max_length=100, null=True, blank=False, default='Please select', db_column='hostype')
    Host_Name = models.CharField(max_length=100, null=True, blank=False, db_column='hostname')
    Source_of_Alert = models.CharField(max_length=100, null=True, blank=False, default='Please select', db_column='source')
    Mode_of_Alert = models.TextField(null=False, default='Manual check', db_column='mode')
    NOC_Engineer = models.CharField(max_length=100, null=True, blank=False, default='Please select', db_column='engineer')
    Remediation = models.TextField(null=True, blank=False, db_column='remediation')
    Escalated = models.CharField(max_length=100, null=False, blank=False, default='No', db_column='escalated')
    Escalated_Reason = models.CharField(max_length=100, null=True, blank=True, default='Please select', db_column='escreason')
    Status = models.CharField(max_length=100, null=True, blank=True, default='Resolved', db_column='status')
    Escalated_to = models.CharField(max_length=100, null=True, blank=False, default='NA', db_column='escalatedto')
    Resolved_by_Team = models.CharField(max_length=100, null=True, blank=False, default='Please select', db_column='resolvedteam')
    Resolved_by_Engineer = models.CharField(max_length=30,null=False, default='noc', db_column='resolvedby')
    Resolution = models.TextField(null=True, blank=False, db_column='resolution')
    Comments = models.TextField(null=True, blank=False, db_column='comments')
    Interval = models.IntegerField(blank=True, null=True, db_column='intrval')
    Complexity = models.TextField(blank=True, null=True, db_column='cmplx')




    #pub_data = models.DateTimeField()
    #image = models.ImageField(upload_to='media/')
    #body = models.TextField()
    #Time_spent = models.TimeField(_(u"Responded Time"), blank=False)
