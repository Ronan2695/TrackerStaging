from . import views
from django.conf.urls import url

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/', views.signupview, name='signup'),
    url(r'^login/', views.loginview, name='login'),
    url(r'^home/', views.homeview, name='home'),
    url(r'^forgot/', views.forgotview, name='forgot'),
    url(r'^usercreated/', views.usercreatedview, name='usercreated'),
]
