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

def create(request):
    if request.method == 'POST':
        if request.POST['process'] == 'register':
            add_user = User.objects.new_user(request)
            if add_user[0] == False:
                request.session['errors'] = add_user[1]
                return redirect('login:index')
            else:
                request.session['name'] = add_user[1].first_name
                request.session['id'] = add_user[1].id
                messages.success(request, 'Successfully registered! Please log in')
                return redirect('ninja:index')

        elif request.POST['process'] == 'login':
            u_log = User.objects.login(request)
            if u_log[0] == True:
                request.session['name'] = u_log[1].first_name
                request.session['id'] = u_log[1].id
                messages.success(request, 'Successfully logged in!')
                return redirect('ninja:index')
            else:
                request.session['errors'] = u_log[1]
                return redirect('login:index')
        else:
            return redirect('login:index')

def show(request):
    return render(request, 'login/success.html')

def logout(request):
    request.session.clear()
    return redirect('/')
