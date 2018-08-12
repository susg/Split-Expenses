from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^signing_up/$', views.signing_up, name='signing_up'),
    url(r'^group/(?P<group_id>[0-9]+)/$', views.group_profile, name='group_profile'),
 	#url(r'^add_expense/(?P<group_id>[0-9]+)/$', views.add_expense, name='add_expense'),
    url(r'^adding_expense/(?P<group_id>[0-9]+)/$', views.adding_expense, name='adding_expense'),
    #url(r'^delete_expense/(?P<group_id>[0-9]+)/$', views.delete_expense, name='delete_expense'),
    url(r'^deleting/(?P<record_id>[0-9]+)/$', views.deleting, name='deleting'),
    #url(r'^deleting/(?P<group_id>[0-9]+)/$', views.deleting, name='deleting'),
    url(r'^create_group/$', views.create_group, name='create_group'),
    url(r'^creating/$', views.creating, name='creating'),
    url(r'^add_member/(?P<group_id>[0-9]+)/$', views.add_member, name='add_member'),
    url(r'^adding_member/(?P<group_id>[0-9]+)/$', views.adding_member, name='adding_member'),
    url(r'^search-autocomplete/$', views.autocompleteModel,  name='search-autocomplete'),
    #url(r'^/$', auth_views.login, name='login'),
]