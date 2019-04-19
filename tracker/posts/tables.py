# tutorial/tables.py
import django_tables2 as tables
from .models import Post
from . import models
from django_tables2.utils import A
from . import views
from django.utils.safestring import mark_safe

class TrackerTable(tables.Table):

    id = tables.Column()
    id = tables.LinkColumn('posts:tracker_view',args=[A('pk')], empty_values=())
    editable = tables.LinkColumn('posts:modify',args=[A('pk')] , empty_values=(), verbose_name='')
    def render_editable(self):
        #return 'Edit'
        return mark_safe('<center><p style="color:blue;">&#9997;</p></center>')

    class Meta:
        model = models.Post
        template_name = 'django_tables2/semantic.html'
        sequence = ('editable','id','...')
        #attrs = {'class': 'table table-bordered', 'tbody': {'id': 'value'}}
        attrs = {'tbody': {'id': 'myTable'}}
