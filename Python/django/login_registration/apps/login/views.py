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
        print '1'*50
        if request.POST['process'] == 'register':
            print '2'*50
            # password = bcrypt.hashpw(request.POST['password'], bcrypt.gensalt())
            # reg_user = {
            #     'first_name' : request.POST['first_name'],
            #     'last_name' : request.POST['last_name'],
            #     'email' : request.POST['email'],
            #     ,
            #     'pw_confirm' :
            # }
            # print reg_user
            add_user = User.objects.new_user(request)
            print '4'*50
            print add_user
            if add_user[0] == False:
                request.session['errors'] = add_user[1]
                return redirect('/')
            else:
                request.session['name'] = add_user[1].first_name
                request.session['id'] = add_user[1].id
                messages.success(request, 'Successfully registered!')
                return redirect('/success')

        elif request.POST['process'] == 'login':
            # pw = bcrypt.generate_password_hash(request.POST['password'])
            login_user = User.object.login(request.POST['email'], pw)
            if login_user[0] == True:
                request.session['name'] = login_user[1].first_name
                request.session['id'] = login_user[1].id
                messages.success(request, 'Successfully logged in!')
                return redirect('/success')
            else:
                request.session['errors'] = login_user[1]

# def login(request):
#     return redirect('/success')

def show(request):
    return render(request, 'login/success.html')
