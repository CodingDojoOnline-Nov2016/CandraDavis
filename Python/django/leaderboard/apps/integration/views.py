from django.shortcuts import render, redirect
from .models import Leaderboard

# Create your views here.
def index(request):
    # user = Leaderboard.objects.all()
    # print '4'*50
    # print user
    # request.session['id'] = user.id
    # context = {
    #     'user': user.first_name
    # }
    # return render('integration:leaderboard', context)
    return redirect('ninja:index')
def update(request):
    if request.method == 'POST':
        # take the total gold count from html and pass it to models to be added to db.
        gold = Leaderboard.update_gold(request.POST, request.session['id'])
        pass
        return redirect('integration:leaderboard')

def show(request):
    top_leaders = Leaderboard.objects.leaders()
    context = {
        'title': 'Current Leaderboard',
        'list_of_leaders': top_leaders,
    }
    return render('integration:leaderboard', context)
# def logout(request):
#     return redirect('login:logout')
