from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.create),
    url(r'^success$', views.show),
    url(r'^delete$', views.destroy)
]
