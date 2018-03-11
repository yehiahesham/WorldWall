from django.conf.urls import *
from django.contrib.auth import views as auth_views
from . import views

app_name = 'wall'

urlpatterns = [
    url(r'^$', views.index.as_view(), name='index'),
    # url(r'^$', views.index.as_view(), name='index'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.Profile.as_view(), name='profile'),
    url(r'^login/$', views.login, name='login'),
    # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
