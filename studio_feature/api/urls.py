from django.conf.urls import url
from api import views
from django.contrib import admin

urlpatterns=[

    url(r'^create/$', views.create_service),
    url(r'^get/$',views.get_service),
    url(r'^update/(?P<pk>[0-9]+)$',views.update_service),
    url(r'^delete/(?P<service>.*)$',views.delete_service),


]
