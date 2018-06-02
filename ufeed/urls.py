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
    url(r'^set_data/$',views.set_data, name='set_data'),
    url(r'^modify/delete_userdata/$', views.all_userdata_delete, name='all_userdata_delete'),
    url(r'^modify/delete_crwaldata/$', views.all_crawldata_delete, name='all_crawldata_delete'),

]
