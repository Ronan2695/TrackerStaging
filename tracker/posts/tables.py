# tutorial/tables.py
import django_tables2 as tables
from .models import Post
from . import models
from django_tables2.utils import A
from . import views

class TrackerTable(tables.Table):

    id = tables.Column()
    id = tables.LinkColumn('posts:tracker_view',args=[A('pk')], empty_values=())

    class Meta:
        model = models.Post
        template_name = 'django_tables2/semantic.html'
        exclude = ['Complexity','Interval','Ticket_Number']
        attrs = {"class": "paleblue"}
