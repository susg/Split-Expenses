from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    #url(r'^/$', auth_views.login, name='login'),
]