from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Login),
    url(r'^login/signin$', views.signin),
    url(r'^login/signup$', views.signup, name='signup'),
    url(r'^login/index$', views.index, name='index'),
    url(r'^profile/$', views.update_profile),
    url(r'^account/logout/$', views.Logout),
]
