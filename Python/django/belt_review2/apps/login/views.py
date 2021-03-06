from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def process(request):
    if request.method == 'POST':
        if request.POST['process'] == 'register':
            add_user = User.objects.new_user(request.POST)
            if add_user[0] == False:
                messages.error(request, add_user[1])
                return redirect('login:index')
            else:
                request.session['user_name'] = add_user[1].user_name
                request.session['u_id'] = add_user[1].id
                messages.success(request, 'Successfully registered!')
                print
                return redirect('books:homepage')

        elif request.POST['process'] == 'login':
            u_log = User.objects.login(request.POST)
            if u_log[0] == True:
                request.session['user_name'] = u_log[1].user_name
                request.session['u_id'] = u_log[1].id
                print '$'*100
                print request.session['u_id']
                messages.success(request, 'Successfully logged in!')
                return redirect('books:homepage')
            else:
                request.session['errors'] = u_log[1]
                return redirect('login:index')
        else:
            return redirect('login:index')

# def show(request):
#     return render(request, 'login/success.html')

# def logout(request):
#     request.session.clear()
#     return redirect('login:index')
