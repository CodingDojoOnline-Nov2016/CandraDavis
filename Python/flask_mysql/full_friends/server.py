from flask import Flask, redirect, request, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
app.secret_key = 'csdavis09'

@app.route('/')
def index():
    friends = mysql.query_db('select * from friends')
    print friends
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    print request.form
    valid_form = True
    if len(request.form['first_name']) < 2 or len(request.form['last_name']) < 2:
        flash('Please enter a valid name')
        valid_form = False
    if len(request.form['email_address']) < 1:
        flash('Email cannot be blank')
        valid_form = False
    elif not EMAIL_REGEX.match(request.form['email_address']):
        flash('You must enter a valid email address')
        valid_form = False
    if valid_form == False:
        session['color'] = 'red'
    elif valid_form == True:
        query = 'INSERT INTO friends(first_name, last_name, email, created_at) VALUES(:first_name, :last_name, :email, now())'
        data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email_address']
        }
        mysql.query_db(query, data)
        flash('Success')
        session['color'] = 'green'
        return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    query = 'SELECT * from friends where id = :id'
    data = { 'id': id }
    friends = mysql.query_db(query, data)
    print friends
    # id = friends[0]['id']
    return render_template('edit.html', id=id, one_friend=friends)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    print request.form
    valid_form = True
    if len(request.form['first_name']) < 2 or len(request.form['last_name']) < 2:
        flash('Please enter a valid name')
        valid_form = False
        # return redirect('/friends/<id>')
    if len(request.form['email']) < 1:
        flash('Email cannot be blank')
        valid_form = False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('You must enter a valid email address')
        valid_form = False
    if valid_form == False:
        session['color'] = 'red'
    elif valid_form == True:
        query = 'UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id'
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'id': id
            }
        mysql.query_db(query, data)
        flash('Success')
        session['color'] = 'green'
        return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
    query = 'DELETE FROM friends WHERE id = :id'
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
