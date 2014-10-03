from django.conf.urls import url

from crawler import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pages/(?P<page_id>\d+)/$', views.getPage, name='getPage'),
    url(r'^pages/$', views.pages, name='create'),
]