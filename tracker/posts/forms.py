from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from . import models
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.db.models.fields import BLANK_CHOICE_DASH
from datetime import date
from bootstrap_datepicker_plus import DatePickerInput
from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput

class CreateArticle(forms.ModelForm):


    Year = forms.IntegerField(widget=forms.NumberInput(attrs={'title':'Enter the current Year'}))

    weeknumber = date.today().isocalendar()[1]
    Week = forms.IntegerField(initial=weeknumber, widget=forms.NumberInput(attrs={'title':'Week number'}))

    shift_choices=(('apac','APAC'),('emea','EMEA'),('usa','USA'))

    Shift = forms.ChoiceField(choices=shift_choices, widget=forms.RadioSelect(attrs={'title':'The shift in which alert was handled'}))

    weekchoice=(('Weekday','Weekday'),('Weekend','Weekend'))
    Day_Of_Week = forms.ChoiceField(choices=weekchoice, widget=forms.RadioSelect)

    Start_Time = forms.IntegerField(widget=forms.DateInput(attrs={'placeholder':'HH:MM','title':'Mention the start time in 24 hour time formant','pattern':'([01]?[0-9]|2[0-3]):[0-5][0-9]'}))
    #placeholder="HH:MM" size="13" title="Enter the time you spent" pattern=".+:.+"/
    Responded_Time = forms.IntegerField(widget=forms.DateInput(attrs={'placeholder':'HH:MM','title':'Mention the Responded time in 24 hour time formant','pattern':'([01]?[0-9]|2[0-3]):[0-5][0-9]'}))

    Time_spent = forms.IntegerField(widget=forms.DateInput(attrs={'placeholder':'HH:MM','title':'Mention the Total time spent in 24 hour time formant','pattern':'([01]?[0-9]|2[0-3]):[0-5][0-9]'}))

    MONTH_CHOICES = (
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December'),
)
    #today = datetime.date.today()
    #months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    #current_month = months[today.month]
    #months = today.month
    Month_empty = tuple(BLANK_CHOICE_DASH + list(MONTH_CHOICES))
    Month = forms.ChoiceField(choices=(Month_empty), widget=forms.Select(attrs={'title':'Enter the current Month'}))

    Res_team = (
    ('B2B - Core', 'B2B - Core'),
    ('B2B - Data', 'B2B - Data'),
    ('B2B - Reporting', 'B2B - Reporting'),
    ('Beehive', 'Beehive'),
    ('BI', 'BI'),
    ('Data Infra', 'Data Infra'),
    ('Data Prod', 'Data Prod'),
    ('Data Science', 'Data Science'),
    ('Dev', 'Dev'),
    ('Dynamic Cretive', 'Dynamic Cretive'),
    ('Facebook', 'Facebook'),
    ('Growth', 'Growth'),
    ('Growth IO', 'Growth IO'),
    ('Internal Tools', 'Internal Tools'),
    ('IT', 'IT'),
    ('NA', 'NA'),
    ('NOC', 'NOC'),
    ('omnom', 'omnom'),
    ('Prospecting', 'Prospecting'),
    ('Rakuten', 'Rakuten'),
    ('RTB', 'RTB'),
    ('Sendroll', 'Sendroll'),
    ('SRE', 'SRE'),
    ('TAM', 'TAM'),
    ('Voltron', 'Voltron'),
    ('Webapp', 'Webapp'),
)
    Res_team_empty =  tuple(BLANK_CHOICE_DASH + list(Res_team))
    Responsible_Team = forms.ChoiceField(choices=(Res_team_empty), widget=forms.Select(attrs={'title':'Enter the Responsible Team'}))

    fse_alarm=(('Yes','Yes'),('No','No'))
    False_Alarm = forms.ChoiceField(choices=fse_alarm, widget=forms.RadioSelect(attrs={'title':'Was the alert genuine?'}))

    inc_type = (
    ('Alert', 'Alert'),
    ('GHC', 'GHC'),
    ('Other', 'Other'),
    ('Security Audit', 'Security Audit'),
    ('Task', 'Task'),
)
    inc_type_empty = tuple(BLANK_CHOICE_DASH + list(inc_type))
    Incident_Type = forms.ChoiceField(choices=(inc_type_empty), widget=forms.Select(attrs={'title':'Enter the type of incident'}))

    prior=(('P0','P0'),('P1','P1'),('P2','P2'),('None','None'))
    Priority = forms.ChoiceField(choices=prior, widget=forms.RadioSelect(attrs={'title':'The priority of alert as per policy'}))



    name = (
    ('Celery Dashboard check', 'Celery Dashboard check'),
    ('Dashboard monitoring', 'Dashboard monitoring'),
    ('Pipeline monitoring', 'Pipeline monitoring'),
    ('Storm Monitoring', 'Storm Monitoring'),
)
    name_empty = tuple(BLANK_CHOICE_DASH + list(name))
    Name = forms.ChoiceField(choices=(name_empty), widget=forms.Select(attrs={'title':'Enter the name of the incident'}))
    #,widget=forms.TextInput(attrs={'title':'last name'})

    If_Others_Please_Specify = forms.CharField(initial=weeknumber, widget=forms.TextInput(attrs={'title':'If you entered others, Please shed some light.'}))

    envi = (
    ('Production', 'Production'),
    ('Staging', 'Staging'),
    ('Test', 'Test'),
    ('Dev', 'Dev'),
    ('Local', 'Local'),
    ('Multiple', 'Multiple'),
    ('NA', 'NA'),
)
    envi_empty = tuple(BLANK_CHOICE_DASH + list(envi))
    Environment = forms.ChoiceField(choices=(envi_empty), widget=forms.Select(attrs={'title':'Enter the incident Environment'}))

    hosttype = (
    ('AWS Batch', 'AWS Batch'),
    ('AWS ECS', 'AWS ECS'),
    ('AWS EC2', 'AWS EC2'),
    ('AWS Elasticache', 'AWS Elasticache'),
    ('emr', 'AWS EMR'),
    ('AWS RDS', 'AWS RDS'),
    ('Batchie Patchie', 'Batchie Patchie'),
    ('Celery Worker', 'Celery Worker'),
    ('Docker Registry', 'Docker Registry'),
    ('Docker Server', 'Docker Server'),
    ('Hbase cluster', 'Hbase cluster'),
    ('Jenkins', 'Jenkins'),
    ('Load Balancer', 'Load Balancer'),
    ('Localhost', 'Localhost'),
    ('Luigi', 'Luigi'),
    ('NA', 'NA'),
    ('Other', 'Other'),
    ('Presto', 'Presto'),
    ('Puppet', 'Puppet'),
    ('puppet', 'Puppet'),
    ('Quentin', 'Quentin'),
    ('Strom cluster', 'Strom cluster'),
    ('Thrift Cluster', 'Thrift Cluster'),
)
    hosttype_empty = tuple(BLANK_CHOICE_DASH + list(hosttype))
    Host_Type = forms.ChoiceField(choices=(hosttype_empty), widget=forms.Select(attrs={'title':'Enter the host type'}))

    source = (
    ('AWS', 'AWS'),
    ('Celery', 'Celery'),
    ('DataDog', 'DataDog'),
    ('Icinga', 'Icinga'),
    ('Jenkins', 'Jenkins'),
    ('Logentries', 'Logentries'),
    ('NA', 'NA'),
    ('New Relic', 'New Relic'),
    ('Pingdom', 'Pingdom'),
    ('Sentry', 'Sentry'),
    ('Slack', 'Slack'),
    ('Threatstack', 'Threatstack'),
)
    source_empty = tuple(BLANK_CHOICE_DASH + list(source))
    Source_of_Alert = forms.ChoiceField(choices=(source_empty), widget=forms.Select(attrs={'title':'Enter the source of alert'}))

    mode=[('Email','Email'),('Manual Check','Manual Check'),('Slack','Slack')]
    Mode_of_Alert = forms.ChoiceField(choices=mode, widget=forms.RadioSelect(attrs={'title':'Enter the mode of alert'}), initial="Manual Check")

    engineer= (
    ('Ajmeer Khaja', 'Ajmeer Khaja'),
    ('Gowtham Perumalsamy', 'Gowtham Perumalsamy'),
    ('Hajamoideen Jailaudeen','Hajamoideen Jailaudeen'),
    ('Irfan Junaid', 'Irfan Junaid'),
    ('MIS team', 'MIS team'),
    ('QA team', 'QA team'),
    ('Rajaram Ganesapandian', 'Rajaram Ganesapandian'),
    ('Ramesh Krishna', 'Ramesh Krishna'),
    ('Rohit Nannan', 'Rohit Nannan'),
    ('Shivani Ramesh', 'Shivani Ramesh'),
    ('Thirumalaibarathi Thangavelu', 'Thirumalaibarathi Thangavelu'),
    ('Umashree Ramesh', 'Umashree Ramesh'),
    ('Vijay Mohan', 'Vijay Mohan'),
)
    engineer_empty = tuple(BLANK_CHOICE_DASH + list(engineer))
    NOC_Engineer = forms.ChoiceField(choices=(engineer_empty),widget=forms.Select(attrs={'title':'The NOC Engineer who handled the incident'}))

    escalate=[('Yes','Yes'),('No','No')]
    #Escalated = forms.ChoiceField(choices=escalate, widget=forms.RadioSelect, initial='no')
    escalate_empty = tuple(BLANK_CHOICE_DASH + list(escalate))
    Escalated = forms.ChoiceField(choices=(escalate_empty), initial='No', widget=forms.Select(attrs={'title':'Was the alert escalated?'}))

    escreason = (
    ('Code level issue', 'Code level issue'),
    ('Configuration Changes', 'Configuration Changes'),
    ('Requesting Remediation', 'Requesting Remediation'),
    ('Unable to Resolve', 'Unable to Resolve'),
    ('Review Needed', 'Review Needed'),
    ('No Access', 'No Access'),
    ('NA', 'NA'),
)
    escreason_empty = tuple(BLANK_CHOICE_DASH + list(escreason))
    Escalated_Reason = forms.ChoiceField(choices=(escreason_empty), required=False, widget=forms.Select(attrs={'title':'The reson for escalation'}))

    stat = (
    ('Resolved', 'Resolved'),
    ('Pending', 'Pending'),
    ('Pending Followup', 'Pending Followup'),
    ('Handed over', 'Handed over')
    )
    stat_empty = tuple(BLANK_CHOICE_DASH + list(stat))
    Status = forms.ChoiceField(choices=(stat_empty),widget=forms.Select(attrs={'title':'Current status of the incident'}))

    escto = (
    ('B2B core', 'B2B core'),
    ('B2B reporting', 'B2B reporting'),
    ('B2B Data', 'B2B Data'),
    ('Beehive', 'Beehive'),
    ('BI', 'BI'),
    ('Data-Infra', 'Data-Infra'),
    ('Data-Prod', 'Data-Prod'),
    ('Data-Sci', 'Data-Sci'),
    ('Dev', 'Dev'),
    ('Dynamic Creative', 'Dynamic Creative'),
    ('Facebook', 'Facebook'),
    ('Growth', 'Growth'),
    ('GrowthIO', 'GrowthIO'),
    ('Internal tools', 'Internal tools'),
    ('IT', 'IT'),
    ('NA', 'NA'),
    ('NOC', 'NOC'),
    ('Omnom', 'Omnom'),
    ('Prospecting', 'Prospecting'),
    ('Rakuten', 'Rakuten'),
    ('RTB', 'RTB'),
    ('Sendroll', 'Sendroll'),
    ('SRE', 'SRE'),
    ('TAM', 'TAM'),
    ('Voltron', 'Voltron'),
    ('Webappp', 'Webappp'),
)
    escto_empty = tuple(BLANK_CHOICE_DASH + list(escto))
    Escalated_to = forms.ChoiceField(choices=(escto_empty), required=False, widget=forms.Select(attrs={'title':'Enter the Team to whom the alert was escalated'}))

    resby = (
    ('B2B core', 'B2B core'),
    ('B2B reporting', 'B2B reporting'),
    ('B2B Data', 'B2B Data'),
    ('Beehive', 'Beehive'),
    ('BI', 'BI'),
    ('Data-Infra', 'Data-Infra'),
    ('Data-Prod', 'Data-Prod'),
    ('Data-Sci', 'Data-Sci'),
    ('Dev', 'Dev'),
    ('Dynamic Creative', 'Dynamic Creative'),
    ('Facebook', 'Facebook'),
    ('Growth', 'Growth'),
    ('GrowthIO', 'GrowthIO'),
    ('Internal tools', 'Internal tools'),
    ('IT', 'IT'),
    ('NA', 'NA'),
    ('NOC', 'NOC'),
    ('Omnom', 'Omnom'),
    ('Prospecting', 'Prospecting'),
    ('Rakuten', 'Rakuten'),
    ('RTB', 'RTB'),
    ('Sendroll', 'Sendroll'),
    ('SRE', 'SRE'),
    ('TAM', 'TAM'),
    ('Voltron', 'Voltron'),
    ('Webappp', 'Webappp'),
)
    resby_empty = tuple(BLANK_CHOICE_DASH + list(resby))
    Resolved_by_Team = forms.ChoiceField(choices=(resby_empty), widget=forms.Select(attrs={'title':'Enter the Team which resolved the alert'}))

    Resolved_by_Engineer = forms.CharField(widget=forms.TextInput(attrs={'title':'The Engineer who resolved the alert'}))

    class Meta:
        model = models.Post
        fields = '__all__'
        field_order = ['Year','Week','Month','Date','Shift','Day_Of_Week','Time','Responded_Time','Time_spent','Complexity','Responsible_Team','False_alarm','Incident_Type','Priority','If_Others_Please_Specify','Description','Environment','Host_Type','Host_Name','Source_of_Alert','Mode_of_Alert','NOC_Engineer','Remediation','Escalated',
        'Escalated_Reason','Status','Escalated_to','Resolved_by_Team','Resolved_by_Engineer','Resolution','Comments']
        exclude = ['Ticket_Number','author']
