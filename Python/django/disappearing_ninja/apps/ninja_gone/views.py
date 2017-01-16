from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'ninja_gone/index.html')

def show(request):
    return render(request, 'ninja_gone/view_ninjas.html')

def post(request):
    print request.method
    messages = []
    context = {
        'messages': messages
    }
    validation = True
    if request.method == 'POST':
        if len(request.POST['pick_color'] < 2) or not unicode.isalpha(request.POST['pick_color']):
            messages.append(messages.error(request, 'Please enter a valid color: Red, Orange, Blue or Purple'))
            validation = False
        if not request.POST['pick_color'].lower() == 'blue'or not request.POST['pick_color'].lower() == 'purple'or not request.POST['pick_color'].lower() == 'red'or not request.POST['pick_color'].lower() == 'orange':
            messages.append(messages.error(request, 'Please enter a valid color: Red, Orange, Blue or Purple'))
            validation = False
        if validation == True:
            request.session['color'] = request.POST['pick_color']
            color = request.session['color']
            return redirect('/ninjas/' + color)
def view(request, color):
    context = {
        'color': color
    }
    return render(request, 'ninja_gone/single_ninja.html', context)
