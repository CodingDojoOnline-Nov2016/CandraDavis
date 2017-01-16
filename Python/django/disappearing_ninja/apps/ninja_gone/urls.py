from django.conf.urls import url
# from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$', views.show),
    url(r'^ninjas/select$', views.post),
    url(r'^ninjas/(?P<color>[a-zA-Z]+)$', views.view),

]
