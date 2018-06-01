from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index, name ='main'),
    url(r'^register/$', views.register, name='register'),
    url(r'^modify/$', views.modify, name='modify'),
    url(r'^notify/$', views.notify, name='notify'),
    url(r'^set_mode/$',views.set_mode, name='set_mode'),
    url(r'^set_data/$',views.set_data, name='set_data'),
    url(r'^modify/(?P<pk>\d+)/edit/$', views.edit, name='edit'),
    url(r'^modify/(?P<pk>\d+)/delete/$', views.delete, name='delete'), #원리 이해 필요할 듯
    #url(r'^modify/delete_crawldata/$', views.delete_crawldata, name='delete_crawldata'),
    url(r'^modify/delete_userdata/$', views.delete_userdata, name='user_delete'),

]
