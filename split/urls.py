from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^group/(?P<group_id>[0-9]+)/$', views.group_profile, name='group_profile'),
 	url(r'^add_record/', views.add_record, name='add_record'),
    #url(r'^/$', auth_views.login, name='login'),
]