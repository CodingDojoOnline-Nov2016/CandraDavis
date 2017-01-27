from django.conf.urls import url
from . import views

app_name = 'ninja'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process_money$', views.create, name='create_gold')
]
