from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'ninja_gone/index.html')

def show(request):
    return render(request, 'ninja_gone/view_ninjas.html')

def post(request):
    print request.method
    validation = True
    if request.method == 'POST':
        if len(request.POST['pick_color']) < 2 or not unicode.isalpha(request.POST['pick_color']):
            messages.error(request, 'Please enter a valid color: Red, Orange, Blue or Purple')
            validation = False
        print request.POST['pick_color']
        if request.POST['pick_color'].lower() == 'blue'or request.POST['pick_color'].lower() == 'purple'or request.POST['pick_color'].lower() == 'red'or request.POST['pick_color'].lower() == 'orange':
            validation = True
        else:
            messages.error(request, 'Please enter a valid color: Red, Orange, Blue or Purple')
            validation = False
        if validation == False:
            print messages
            context = {
                'messages': messages
            }
            return redirect('/ninjas', context)
        else:
            validation == True
            request.session['color'] = request.POST['pick_color']
            color = request.session['color']
            return redirect('/ninjas/' + color)
def view(request, color):
    context = {
        'color': color
    }
    print color
    return render(request, 'ninja_gone/single_ninja.html', context)
