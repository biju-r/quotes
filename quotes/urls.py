# Created: 05/02/2015   Modified: 05/09/2015

# Author: Vipul Borikar

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]