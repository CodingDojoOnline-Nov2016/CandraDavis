from django.conf.urls import url
from . import views

app_name = 'login'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process$', views.process, name='create'),
    # url(r'^success$', views.show),
    # url(r'^logout$', views.logout),
]
