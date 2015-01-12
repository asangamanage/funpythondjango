from django.conf.urls import patterns, url
from funapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
