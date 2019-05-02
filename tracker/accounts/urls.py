from . import views
from django.conf.urls import url
from django.conf.urls import url, include
import accounts.views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/', views.signupview, name='signup'),
    url(r'^login/', views.loginview, name='login'),
    url(r'^home/', views.homeview, name='home'),
    url(r'^forgot/', views.forgotview, name='forgot'),
    url(r'^usercreated/', views.usercreatedview, name='usercreated'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
