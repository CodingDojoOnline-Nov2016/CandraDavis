from django.conf.urls import url
from . import views

app_name = 'login'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process$', views.create, name='create_log_reg'),
    url(r'^success$', views.show, name='show'),
    url(r'^logout$', views.logout, name='logout'),
]
