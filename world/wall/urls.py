from django.conf.urls import *
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views

app_name = 'wall'

urlpatterns = [
    url(r'^$', views.index.as_view(), name='home'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^users/(?P<pk>[0-9]+)/$', views.Profile, name='profile'),
    url(r'signup/', views.SignUp, name='signup'),
    url(r'^publish/$', views.publish, name='publish'),
]
