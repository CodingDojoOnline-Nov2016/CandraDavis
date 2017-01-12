from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'csdavis09'
import random
@app.route('/')
def set_random_num():
    try:
        session['random_num']
    except:
        session['random_num'] = random.randint(1, 101)
    print session['random_num']
    return render_template('num_game.html')

@app.route('/input_num', methods=['GET', 'POST'])
def input_number():
    print request.form
    session['guess_entered'] = request.form['guess']
    try:
        int(session['guess_entered'])
    except:
        session['message'] = 'Can only accept numbers.'
        return redirect('/')
    if int(session['guess_entered']) <= 0 or int(session['guess_entered']) >= 101:
        session['message'] = 'Please use a valid number!'
    elif int(session['guess_entered']) < session['random_num']:
        session['message'] = 'Sorry! Your guess was too low!  Try again.'
        session['color'] = 'red'
    elif int(session['guess_entered']) > session['random_num']:
        session['message'] = 'Sorry! Your guess was too high!  Try again.'
        session['color'] = 'red'
    elif int(session['guess_entered']) == session['random_num']:
        session['message'] = 'You rock! Your guess was right!'
        session['color'] = 'green'
    print session['random_num']
    return redirect('/')
app.run(debug=True)
# @app.route('/reset')
# def reset():
#     session['count'] = 0
#     count = session['count']
#     while count < 4:
#         count += 1
#         if count == 4:
#             return redirect('/')
