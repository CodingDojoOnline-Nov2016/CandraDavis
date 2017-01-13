from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'surveyForm/index.html')

def create(request):
    if request.method == 'POST':
        print request.POST
        if len(request.POST['full_name']) <= 2:
            messages.error(request, 'Please enter a valid first and last name.')
            return redirect('/')
        elif len(request.POST['comment']) > 120:
            messages.error(request, 'Please enter a comment 120 characters or less.')
            return redirect('/')
        else:
            request.session['name'] = request.POST['full_name']
            request.session['location'] = request.POST['location']
            request.session['fav_lang'] = request.POST['fav_lang']
            request.session['comment'] = request.POST['comment']
            return redirect('/results')
    else:
        request.method == 'GET'
        return redirect('/')

def show(request):
    try:
        request.session['count'] += 1
    except:
        request.session['count'] = 1
    messages.success(request, 'Thanks for submitting this form!  You have submitted this form {}'.format(request.session['count'])+ ' times now.')
    context = {
        'name': request.session['name'],
        'location': request.session['location'],
        'fav_lang': request.session['fav_lang'],
        'comment': request.session['comment']
    }
    return render(request, 'surveyForm/results.html', context)
