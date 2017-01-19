from django.shortcuts import render, redirect, HttpResponse
from .models import Email, EmailManager
from django.contrib import messages

# Create your views here.
def index(request):
    try:
        request.session['errors']
    except KeyError:
        request.session['errors'] = []
    return render(request, 'validEmail/index.html')

def create(request):
    if request.method == 'POST':
        new_email = Email.objects.valid_email(request.POST['email'])
        print new_email
        if new_email(0) == False:
            request.session['errors'].append(new_email(1))
            return redirect('/')
        else:
            request.session['email'] = new_email[1].email
            messages.success(request, "The email address you entered {}".format(request.session['email']) + " is a VALID email.  Thank you!" )
            return redirect('/success')

def show(request):
    context = {
    'emails' : Email.objects.all()
    }
    return render(request, 'validEmail/show.html', context)
