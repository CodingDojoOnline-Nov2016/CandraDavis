from flask import Flask, session, redirect, render_template, flash, request
import re
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'csdavis09'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/postUserInfo', methods=['POST'])
def postUserInfo():
    print request.form
    valid_form = True
    if len(request.form['first-name']) < 1:
        flash('Please enter a valid first name')
        valid_form = False
    elif len(request.form['last-name']) < 1:
        flash('Please enter a valid last name')
        valid_form = False
    else:
        flash('Success! You entered: {}{}'.format(request.form['first-name'], request.form['last-name']))
    if len(request.form['create-password']) < 8:
        flash('Please enter a password with more than 8 characters')
        valid_form = False
    elif not request.form['create-password'] == request.form['password-confirm']:
        flash('You must enter matching passwords')
        valid_form = False
    else:
        flash('Success!')
    if len(request.form['email']) < 1:
        flash('Email cannot be blank')
        valid_form = False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('You must enter a valid email address')
        valid_form = False
    else:
        flash('Success!')
    if valid_form == True:
        session['firstname'] = request.form['first-name']
        session['lastname'] = request.form['last-name']
        session['email'] = request.form['email']
        return redirect('/result')
    else:
        return redirect('/')
@app.route('/result')
def post_user():
    return render_template('results.html')
app.run(debug=True)
