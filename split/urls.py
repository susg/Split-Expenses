from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^group/(?P<group_id>[0-9]+)/$', views.group_profile, name='group_profile'),
 	url(r'^add_expense/(?P<group_id>[0-9]+)/$', views.add_expense, name='add_expense'),
    url(r'^adding/(?P<group_id>[0-9]+)/$', views.adding, name='adding'),
    url(r'^delete_expense/(?P<group_id>[0-9]+)/$', views.delete_expense, name='delete_expense'),
    url(r'^deleting/(?P<group_id>[0-9]+)/$', views.deleting, name='deleting'),
    url(r'^create_group/$', views.create_group, name='create_group'),
    url(r'^creating/$', views.creating, name='creating'),
    
    #url(r'^/$', auth_views.login, name='login'),
]