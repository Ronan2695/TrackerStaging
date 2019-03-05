from django.contrib import admin
from django.conf.urls import url, include
import accounts.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^posts/', include('posts.urls')),
]
