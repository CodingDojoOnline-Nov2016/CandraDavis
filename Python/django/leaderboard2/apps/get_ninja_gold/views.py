from django.shortcuts import render, redirect
import random, datetime
from ..integration2.models import Leaderboard

def index(request):
    #set the gold count to zero on first page load.
    try:
        request.session['count']
        request.session['total_gold']
        request.session['results']
    except KeyError:
        request.session['count'] = 0
        request.session['total_gold'] = 0
        request.session['results'] = []

    context = {
        'title' : 'Ninja Gold'
    }

    return render(request, 'get_ninja_gold/index.html', context)
def process(request):
    if request.method == 'POST':
        print request.POST
        time_now = datetime.datetime.now().strftime('%Y/%m/%d %I:%M%p')
        print time_now
        gold = 0

        request.session['count'] += 1

        # a dictionary to hold all of the results from each building.
        loc_activity = {}
        loc_activity['time'] = time_now

        if request.POST['building'] == 'farm':
            gold = random.randint(10, 20)
            request.session['total_gold'] += gold
            loc_activity['building'] = 'farm'
            loc_activity['gold'] = gold
            loc_activity['color'] = 'green'


        elif request.POST['building'] == 'cave':
            gold = random.randint(5, 10)
            request.session['total_gold'] += gold
            loc_activity['building'] = 'cave'
            loc_activity['gold'] = gold
            loc_activity['color'] = 'green'


        elif request.POST['building'] == 'house':
            gold = random.randint(2, 5)
            request.session['total_gold'] += gold
            loc_activity['building'] = 'house'
            loc_activity['gold'] = gold
            loc_activity['color'] = 'green'


        elif request.POST['building'] == 'casino':
            gold = random.randint(-50, 50)
            request.session['total_gold'] += gold
            loc_activity['building'] = 'casino'
            loc_activity['gold'] = gold

            if gold > 0:
                loc_activity['color'] = 'green'
            else:
                loc_activity['color'] = 'red'
            print loc_activity

    request.session['results'].append(loc_activity)
    print request.session['results']
    return redirect('/')

def update(request):
    # save_gold = Leaderboard.objects.get(id=request.session['id'])
    update_gold = {
        'add_gold_to_total_gold': request.session['total_gold'],
        'num_games': request.session['count'],
        'new_top_score': request.session['total_gold'],
        'id': request.session['id']
        }
    u_update = Leaderboard.objects.save_gold(update_gold)
    context = {
        "new_totals": u_update,
    }
    print u_update.top_score
    # request.session.clear(['total_gold'])
    return render(request, 'get_ninja_gold/index.html', context)
