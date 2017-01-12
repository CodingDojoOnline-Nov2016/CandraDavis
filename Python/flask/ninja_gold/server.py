from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "csdavis09"
import random, datetime
@app.route('/')
def index():
    try:
        session['gold_count']
    except KeyError:
        session['gold_count'] = 0
    return render_template('ninja_gold.html')
@app.route('/process_money', methods=['POST'])
def money():
    print request.form
    current_gold = 0
    if not 'activities' in session:
        session['activities'] = []
    activity = {'location': None,
    'current_gold': None,
    'time_added': None}
    if request.form['location'] == 'farm':
        current_gold = random.randint(10, 21)
        session['gold_count'] += current_gold
        activity['current_gold'] = current_gold
        activity['location'] = request.form['location']
        activity['time_added'] = datetime.datetime.now()
        print activity
    elif request.form['location'] == 'cave':
        current_gold = random.randint(5, 11)
        session['gold_count'] += current_gold
        activity['current_gold'] = current_gold
        activity['location'] = request.form['location']
        activity['time_added'] = datetime.datetime.now()
        print activity

    elif request.form['location'] == 'house':
        current_gold = random.randint(2, 6)
        session['gold_count'] += current_gold
        activity['current_gold'] = current_gold
        activity['location'] = request.form['location']
        activity['time_added'] = datetime.datetime.now()
        print activity

    elif request.form['location'] == 'casino':
        current_gold = random.randint(-50, 51)
        session['gold_count'] += current_gold
        activity['current_gold'] = current_gold
        activity['location'] = request.form['location']
        activity['time_added'] = datetime.datetime.now()
        print activity
    if current_gold < 0:
        ['color'] = 'red'
    else:
        ['color'] = 'green'
    session['activities'].append(activity)
    return redirect('/')

app.run(debug=True)
