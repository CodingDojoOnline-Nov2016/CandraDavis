print 'I will be your future routes; HTTP requestes will be captured by me.'
from django.conf.urls import url
from . import views

def method_to_run(request):
    print 'Whatever route that was hit by a HTTP request (by the way) decided to invoke me'
    print 'By the way, here is the request object that Django automatically passes us: ', request
    print 'By the way, we still are not delivering anything to the browser, so you should see a "Value Error at /"'

urlpatterns = [
    url(r'^', views.index)
]
