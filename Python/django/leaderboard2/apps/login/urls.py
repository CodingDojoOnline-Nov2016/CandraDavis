from django.conf.urls import url
from . import views

app_name = 'login'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process$', views.process, name='process'),
    url(r'^success$', views.show, name='user_info'),
    url(r'^logout$', views.logout, name='logout'),
]
