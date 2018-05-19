from django.conf.urls import url
from papers import views

urlpatterns = [
    url(r'^papers/$', views.paper_list),
    url(r'^papers/(?P<pk>[0-9]+)/$', views.paper_detail),
]
