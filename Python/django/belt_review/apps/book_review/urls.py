from django.conf.urls import url
from . import views

app_name = 'books'
urlpatterns = [
    url(r'^$', views.index, name='login-index'),
    url(r'^books$', views.show, name='homepage'),
    url(r'^books/add$', views.create, name='add_books'),
    url(r'^books/add/process$', views.update, name='update'),
    url(r'^books/(?P<b_id>[d]+)$', views.show_book, name='show_book'),
    url(r'^books/logout$', views.logout, name='logout'),
    url(r'^users/(?P<u_id>[d]+)$', views.show_user, name='user_page')
]
