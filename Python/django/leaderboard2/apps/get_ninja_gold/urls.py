from django.conf.urls import url
from . import views

app_name = 'ninja'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process_money$', views.process, name='add_money'),
    url(r'^update$', views.update, name='save_money')
]
