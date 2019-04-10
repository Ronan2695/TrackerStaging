from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from . import models
from django_tables2.utils import A
from . import views

class FilteredPersonListView(SingleTableMixin, FilterView):
    table_class = TrackerTable
    model = models.Post
    template_name = 'posts/tracker_list.html'

    filterset_class = PersonFilter
