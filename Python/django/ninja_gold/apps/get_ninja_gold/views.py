from django.shortcuts import render, redirect
import random, datetime


def index(request):
    try:
        request.session['total_gold']
    except KeyError:
        request.session['total_gold'] = 0
    context = {
        'title' : 'Ninja Gold',
        'total_gold' : request.session['total_gold']
    }
    return render(request, 'get_ninja_gold/index.html', context)
def post(request):
    if request.method == 'POST':
        print request.POST
        now = datetime.datetime.now().strftime('%Y/%m/%d %I:%M%p')
        print now
        total_gold = request.session['total_gold']
        gold = 0
        activities = []
        loc_activity = {
            'building': None,
            'gold': None,
            'time': None,
            'color': None
        }
        try:
            request.session['activities']
        except KeyError:
            request.session['activities'] = []

        if request.POST['building'] == 'farm':
            gold = random.randint(10, 20)
            total_gold += gold
            loc_activity['building'] = 'farm'
            loc_activity['gold'] = gold
            loc_activity['time'] = now
            loc_activity['color'] = 'green'
            print loc_activity
        elif request.POST['building'] == 'cave':
            gold = random.randint(5, 10)
            total_gold += gold
            loc_activity['building'] = 'cave'
            loc_activity['gold'] = gold
            loc_activity['time'] = now
            loc_activity['color'] = 'green'
            print loc_activity
        elif request.POST['building'] == 'house':
            gold = random.randint(2, 5)
            total_gold += gold
            loc_activity['building'] = 'house'
            loc_activity['gold'] = gold
            loc_activity['time'] = now
            loc_activity['color'] = 'green'
            print loc_activity
        elif request.POST['building'] == 'casino':
            gold = random.randint(-50, 50)
            total_gold += gold
            loc_activity['building'] = 'casino'
            loc_activity['gold'] = gold
            loc_activity['time'] = now
            if gold > 0:
                loc_activity['color'] = 'green'
            else:
                loc_activity['color'] = 'red'
            print loc_activity
    request.session['activities'] = activities.append(loc_activity)

    return redirect('/')
