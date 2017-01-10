from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'csdavis09'
mysql = MySQLConnector(app, 'login_register')
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def login_signup():
    return render_template('login.html')
@app.route('/create_user', methods=['POST'])
def create_user():
    print request.form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    user_pw = request.form['password']
    pw_confirm = request.form['password_confirm']
    validation = True
    if len(first_name) < 2 or len(last_name) < 2:
        flash('Please enter a valid name')
        validation = False
    if len(email) < 1:
        flash('User email can not be empty')
        validation = False
    elif not EMAIL_REGEX.match(email):
        flash('Please enter a valid email address')
        validation = False
    if len(user_pw) < 8:
        flash('Password must be at least 8 characters')
        validation = False
    elif not user_pw == pw_confirm:
        validation = False
    if validation == True:
        pw_hash = bcrypt.generate_password_hash(user_pw)
        query = 'INSERT INTO users(first_name, last_name, email, pw_hash, created_at, updated_at) VALUES(:first_name, :last_name, :email, :pw_hash, NOW(), NOW())'
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'pw_hash': pw_hash
        }
        mysql.query_db(query, data)
        flash('You have successfully created a new account')
        coloration = 'green'
        return redirect('/index/<id>')
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
    if bcrypt.check_password_hash(check_user[0]['pw_hash'], password):
        return redirect('/index/' + str(check_user[0]['id']))        
    else:
        flash('Incorrect user email or password')
        validation = False
        return redirect('/')
@app.route('/index/<id>')
def index(id):
    query = 'SELECT * FROM users WHERE id = :id'
    data = { 'id': id }
    user = mysql.query_db(query, data)
    print user
    # session['id'] = user[0]['id']
    return render_template('index.html', id=id, user=user)
app.run(debug = True)
