from django.conf.urls import url
from . import views

app_name = 'integration'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^update$', views.update, name='update'),
    url(r'^leaderboard$', views.show, name='leaderboard'),
    # url(r'^logout$', views.logout, name='logout')
]
