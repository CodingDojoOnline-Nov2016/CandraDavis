from django.shortcuts import render, redirect
from .models import Leaderboard
# Create your views here.
def index(request):
    return redirect('ninja:index')
def show(request):
    # top_leaders = Leaderboard.objects.leaders()
    context = {
        'top_leaders': Leaderboard.objects.order_by(total_gold_earned)[:25],
        'title': 'Top 25 Leaderboard',
    }
    return render(request, 'integration2/leaderboard.html', context)
