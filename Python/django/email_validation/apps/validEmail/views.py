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
        if new_email[0] == False:
            request.session['errors'] = (new_email[1])
            return redirect('/')
        else:
            request.session['email'] = new_email[1].email
            request.session['id'] = new_email[1].id
            print request.session['id']
            messages.success(request, "The email address you entered {}".format(request.session['email']) + " is a VALID email.  Thank you!" )
            return redirect('/success')

def show(request):
    context = {
    'emails' : Email.objects.all()
    }
    return render(request, 'validEmail/show.html', context)

def destroy(request):
    print '3'*50
    print request.session['id']
    email_del = Email.objects.delete_email(request.session['id'])
    if email_del[0] == True:
        messages.success(request, 'Email deleted')
    else:
        messages.error(request, email_del[1])
    return redirect('/success')
