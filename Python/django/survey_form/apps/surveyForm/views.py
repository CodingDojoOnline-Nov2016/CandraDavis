from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'surveyForm/index.html')

def create(request):
    if request.method == 'POST':
        print request.POST
        if len(request.POST <= 2):
            messages.error(request, 'Please enter a valid first and last name.')
        elif len(request.POST['comment'] > 120):
            messages.error(request, 'Please enter a comment 120 characters or less.')
        else:
            try:
                request.session['count']
            except:
                request.session['count'] += 1
                request.session['name'] = request.POST['full_name']
                request.session['location'] = request.POST['location']
                request.session['fav_lang'] = request.POST['fav_lang']
                request.session['comment'] = request.POST['comment']
                messages.success(request, 'Thanks for submitting this form!  You have submitted this form {}'.request.session['count'] + ' times now.')
                return redirect(request, '/results')
    else:
        request.method == 'GET'
        return return(request, 'surveyForm/results.html')
