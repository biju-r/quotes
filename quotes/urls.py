# Created: 05/02/2015   Modified: 05/17/2015

# Author: Vipul Borikar

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^signup$', views.user_creation, name='user_creation'),

]