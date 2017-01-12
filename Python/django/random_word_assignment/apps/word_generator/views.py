from django.shortcuts import render, redirect, HttpResponse
import random
import string

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    return render(request, 'word_generator/index.html')
def create(request):
    print request.method
    if request.method == 'POST':
        print '7'*50
        print request.POST
        n_char = 14
        random_word = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n_char))
        if 'random_word' not in request.session:
            request.session['random_word'] = random_word
        else:
                request.session['random_word'] = random_word
        return redirect('/')
    else:
        if request.method == 'GET':
            return redirect('/')
# Create your views here.
