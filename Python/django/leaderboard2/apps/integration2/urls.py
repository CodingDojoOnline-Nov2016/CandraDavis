from django.conf.urls import url
from . import views

app_name = 'integration2'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^leaderboard$', views.show, name='leaders'),
]
