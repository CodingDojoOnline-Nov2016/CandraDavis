from flask import Flask, session, redirect, render_template, request
app = Flask(__name__)
app.secret_key = "csdavis09"
# count = session['count']
@app.route('/')
def view_count():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('counter.html')
@app.route('/count2', methods=['POST'])
def add2():
    session['count'] += 1
    return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')
app.run(debug=True)
