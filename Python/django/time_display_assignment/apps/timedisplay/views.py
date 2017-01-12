from django.shortcuts import render, HttpResponse
import datetime
# from django.utils import timezone
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    
    context = {
    'now': now
    }
    print 'The request is running!'
    return render(request, 'timedisplay/index.html', context)
