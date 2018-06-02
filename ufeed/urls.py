from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='main'),
    url(r'^index/$', views.index, name ='main'),
    url(r'^register/$', views.register, name='register'),
    url(r'^modify/$', views.modify, name='modify'),
    url(r'^modify/(?P<pk>\d+)/edit/$', views.edit, name='edit'),
    url(r'^modify/(?P<pk>\d+)/delete/$', views.delete, name='delete'),
    url(r'^notify/$', views.notify, name='notify'),
]
