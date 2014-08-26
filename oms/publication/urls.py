__author__ = 'Ga Go'
from django.conf.urls import *

from publication import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<publication_id>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^add_property/$', views.add_property, name='add_property'),
    url(r'^update/(?P<publication_id>\d+)/$', views.update, name='update'),
    ]
