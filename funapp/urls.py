from django.conf.urls import patterns, url
from funapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(<question_id>\d+)/$', views.detail, name='detail'),
)
