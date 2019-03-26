from . import views
from django.conf.urls import url

app_name = 'posts'

urlpatterns = [
    url(r'^schedule/', views.scheduleview, name='schedule'),
    #url(r'^processupdates/', views.prupdatesview, name='prupdates'),
    url(r'^quicklinks/', views.quicklinkview, name='quicklinks'),
    url(r'^tracker_edit/', views.tracker_edit, name='tracker_edit'),
    url(r'^tracker_list/', views.tracker_list, name='tracker_list'),
    url(r'^(?P<track_id>[0-9]+)/$', views.tracker_view, name="tracker_view"),
    #url(r'^modify/(?P<id>[0-9]+)', views.tracker_edit, name="modify"),
]
