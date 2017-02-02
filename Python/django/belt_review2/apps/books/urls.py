from django.conf.urls import url
from . import views

app_name='books'

urlpatterns = [
    url(r'^$', views.index, name='login_index'),
    url(r'^books$', views.show, name='homepage'),
    url(r'^books/add$', views.new_book, name='new_book'),
    url(r'^books/create$', views.create, name='create_new_book'),
    url(r'^books/(?P<b_id>\d+)$', views.show_book, name='show_book'),
    url(r'^books/(?P<b_id>d+)/update$', views.new_review, name='new_review'),
    url(r'^books/review/destroy$', views.delete_review, name='delete_review'),
    url(r'^users/(?P<u_id>\d+)$', views.user_reviews, name='user_reviews'),
    url(r'^books/logout$', views.logout, name='logout')
]
