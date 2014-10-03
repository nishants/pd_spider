from django.conf.urls import url
from crawler import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pages/(?P<page_id>\d+)/$', views.page, name='getAndModify'),
    url(r'^pages/$', views.pages, name='createAndList'),
]