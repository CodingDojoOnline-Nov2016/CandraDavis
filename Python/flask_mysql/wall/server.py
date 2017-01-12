from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app=Flask(__name__)
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app.secret_key = 'csdavis09'
mysql = MySQLConnector(app, 'the_wall')

@app.route('/')
def root():
    return render_template('login.html')
@app.route('/create_user', methods=['POST'])
def create():
    print request.form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    pass_confirm = request.form['password_confirm']
    validation = True
    if len(first_name) < 2 or len(last_name) < 2:
        flash('Please enter a valid name')
        validation = False
    elif not unicode.isalpha(first_name) or not unicode.isalpha(last_name):
        flash('Please enter a valid name')
        validation = False
    if len(email) < 1 or not EMAIL_REGEX.match(email):
        flash('Please enter a valid email address')
        validation = False
    if len(password) < 8 or not password == pass_confirm:
        flash('Please enter a matching password. Password must be at least 8 characters')
        validation = False
    if validation == True:
        pw_hash = bcrypt.generate_password_hash(password)
        query = 'INSERT INTO users(first_name, last_name, email, pw_hash, created_at, updated_at) VALUES(:first_name, :last_name, :email, :pw_hash, NOW(), NOW())'
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'pw_hash': pw_hash
        }
        mysql.query_db(query, data)
        flash('You have successfully created a new account. Please login')
        coloration = 'green'
        return redirect('/')
    else:
        coloration = 'red'
        return redirect('/')
@app.route('/login', methods=['POST'])
def login():
    print request.form
    email = request.form['email']
    password = request.form['password']
    query = 'SELECT * FROM users WHERE email = :email LIMIT 1'
    data = { 'email': email }
    check_user = mysql.query_db(query, data)
    print check_user
    session['user_id'] = check_user[0]['id']
    session['name'] = check_user[0]['first_name']
    if bcrypt.check_password_hash(check_user[0]['pw_hash'], password):
        return redirect('/wall/'+ str(check_user[0]['id']))     # + str(check_user[0]['id']
    else:
        flash('Incorrect user email or password')
        validation = False
        return redirect('/')
@app.route('/wall/<id>')
def index(id):
    query = 'SELECT users.first_name, users.last_name, messages.message, messages.updated_at, messages.id FROM users JOIN messages ON users.id = messages.user_id ORDER BY messages.updated_at DESC'
    messages = mysql.query_db(query)
    return render_template('index.html', id=id, all_messages=messages, name=session['name'])
@app.route('/wall/<id>/new_message', methods=['POST'])
def new_message(id):
    print request.form
    message = request.form['post_message']
    query = 'INSERT INTO messages(message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(),  :user_id)'
    data = {
        'message': message,
        'user_id': session['user_id']
    }
    mysql.query_db(query, data)
    return redirect ('/wall/<id>')
@app.route('/wall/<id>/comment')
def view_comments(id):
    query = 'SELECT users.first_name, users.last_name, messages.message, messages.updated_at, messages.id FROM messages  JOIN users ON users.id = messages.user_id WHERE messages.id = :id'
    data = {
        'id': id
    }
    one_message = mysql.query_db(query, data)
    query = 'SELECT users.first_name, users.last_name, comments.text FROM users JOIN comments ON users.id = comments.user_id WHERE comments.message_id = :id ORDER BY comments.updated_at ASC'
    data = {
    'id': id
    }
    comments = mysql.query_db(query, data)
    print '='*50
    print comments
    print id
    print one_message
    return render_template('comments.html', all_comments=comments, id=id, one_message=one_message, name=session['name'])
@app.route('/wall/<id>/comment', methods=['POST'])
def make_comment(id):
    print id
    text = request.form['post_comment']
    query = 'INSERT INTO comments(text, created_at, updated_at, message_id, user_id) VALUES(:text, NOW(), NOW(), :message_id, :user_id )'
    data = {
        'text': text,
        'message_id': id,
        'user_id': session['user_id']
    }
    add_comment = mysql.query_db(query, data)
    return redirect('/wall/'+ id + '/comment')

app.run(debug=True)
