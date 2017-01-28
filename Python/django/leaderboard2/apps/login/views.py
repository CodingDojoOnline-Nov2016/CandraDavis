from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

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
            add_user = User.objects.new_user(request)
            if add_user[0] == False:
                request.session['errors'] = add_user[1]
                print 'registration error!!!!!!'
                return redirect('login:index')
            else:
                request.session['name'] = add_user[1].first_name
                request.session['id'] = add_user[1].id
                messages.success(request, 'Successfully registered!')
                print 'registered!!!!'
                return redirect('ninja:index')

        elif request.POST['process'] == 'login':
            u_log = User.objects.login(request)
            if u_log[0] == True:
                request.session['name'] = u_log[1].first_name
                request.session['id'] = u_log[1].id
                messages.success(request, 'Successfully logged in!')
                print 'login success'
                return redirect('ninja:index')
            else:
                print 'login error'
                request.session['errors'] = u_log[1]
                return redirect('login:index')

    else:
        return redirect('login:index')

def show(request):
    return render(request, 'login/success.html')

def logout(request):
    try:
        request.session.clear()
        print 'you have hit logout request'
        messages.success(request, 'You have successfully logged out')
    except KeyError:
        print 'you have already processed the logout'
        messages.error(request, 'You have already signed out')
    return redirect('ninja:index')
