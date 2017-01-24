from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, UserManager

# Create your views here.
def index(request):
    try:
        request.session['errors']
    except KeyError:
        request.session['errors'] = []
    return render(request, 'login/index.html')

def process(request):
    if request.method == 'POST':
        if request.POST['process'] == 'register':
            add_user = User.objects.new_user(request.POST)
            if add_user[0] == False:
                request.session['errors'] = add_user[1]
                return redirect('/')
            else:
                request.session['name'] = add_user[1].first_name
                request.session['id'] = add_user[1].id
                messages.success(request, 'Successfully registered!')
                return redirect('/success')

        elif request.POST['process'] == 'login':
            login_user = User.objects.login(request.POST)
            if login_user[0] == True:
                request.session['name'] = login_user[1].first_name
                request.session['id'] = login_user[1].id
                messages.success(request, 'Successfully logged in!')
                return redirect('/success')
            else:
                request.session['errors'] = login_user[1]
                return redirect('/')
        else:
            return redirect('/')

def show(request):
    return render(request, 'login/success.html')
