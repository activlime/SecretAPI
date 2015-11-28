from django.conf.urls import include, url
from django.contrib import admin

from secrets import views

urlpatterns = [
    url(r'^(?P<secret_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.ownsecrets, name='secrets'),
    url(r'^accounts/$', views.accounts, name='accounts'),
    url(r'', include('tokenapi.urls'))
]