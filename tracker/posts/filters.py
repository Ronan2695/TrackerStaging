from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from . import models
from django_tables2.utils import A
from . import views
from django.contrib.auth.models import User
import django_filters

class TrackerFilter(django_filters.FilterSet):
    class Meta:
        model = models.Post
        fields = '__all__'
        #fields = ['Status']

class PendingFilter(django_filters.FilterSet):
    #Status = django_filters.CharFilter(field_name='Status', lookup_expr='exact', initial='Pending')
    class Meta:
        model = models.Post
        #fields = '__all__'
        fields = ['Status']

    def __init__(self, *args, **kwargs):
        super(PendingFilter, self).__init__(*args, **kwargs)
        self.form.initial['Status'] = "pending"
