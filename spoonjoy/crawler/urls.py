from django.conf.urls import url

from crawler import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]