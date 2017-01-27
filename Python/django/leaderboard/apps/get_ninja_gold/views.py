from django.shortcuts import render, redirect
import random, datetime


def index(request):
    try:
        request.session['errors']
    except KeyError:
        request.session['errors'] = []
    try:
        request.session['total_gold']
    except KeyError:
        request.session['total_gold'] = 0
    #set up empty list to gather activites
    try:
        request.session['results']
    except KeyError:
        request.session['results'] = []

    try:
        request.session['count'] += 1
    except KeyError:
        request.session['count'] = 0
    if request.session['count'] >= 5:
        return redirect('login:index')
    else:
        return render(request, 'get_ninja_gold/index.html')
def create(request):
    if request.method == 'POST':
        print request.POST
        time_now = datetime.datetime.now().strftime('%Y/%m/%d %I:%M%p')
        print time_now
        gold = 0
        # a dictionary to hold all of the results from each building.
        loc_activity = {
            'building': None,
            'gold': None,
            'time': None,
            'color': None
            }

        if request.POST['building'] == 'farm':
            gold = random.randint(10, 20)
            request.session['total_gold'] += gold
            loc_activity['building'] = 'farm'
            loc_activity['gold'] = gold
            loc_activity['time'] = time_now
            loc_activity['color'] = 'green'

        elif request.POST['building'] == 'cave':
            gold = random.randint(5, 10)
            request.session['total_gold'] += gold
            loc_activity['building'] = 'cave'
            loc_activity['gold'] = gold
            loc_activity['time'] = time_now
            loc_activity['color'] = 'green'

        elif request.POST['building'] == 'house':
            gold = random.randint(2, 5)
            request.session['total_gold'] += gold
            loc_activity['building'] = 'house'
            loc_activity['gold'] = gold
            loc_activity['time'] = time_now
            loc_activity['color'] = 'green'

        elif request.POST['building'] == 'casino':
            gold = random.randint(-50, 50)
            request.session['total_gold'] += gold
            loc_activity['building'] = 'casino'
            loc_activity['gold'] = gold
            loc_activity['time'] = time_now
            if gold > 0:
                loc_activity['color'] = 'green'
            else:
                loc_activity['color'] = 'red'
            print loc_activity
    request.session['results'].append(loc_activity)
    print request.session['results']
    return redirect('ninja:index')
