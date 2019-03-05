from . import views
from django.conf.urls import url

app_name = 'posts'

urlpatterns = [
    url(r'^schedule/', views.scheduleview, name='schedule'),
    url(r'^processupdates/', views.prupdatesview, name='prupdates'),
    url(r'^nonpd/', views.nonpdview, name='nonpd'),
    url(r'^quicklinks/', views.quicklinkview, name='quicklinks'),
]
