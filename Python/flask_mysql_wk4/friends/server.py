from flask import Flask, redirect, request, render_template, session, flash
from mysqlconnections import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
app.secret_key = 'csdavis09'

@app.route('/')
def index():
    friends = mysql.query_db('select * from friends')
    print friends
    return render_template('index.html', all_friends=friends)

@app.route('/friends/<friend_id>')
def show(friend_id):
    query = 'select * from friends where id = :id'
    data = { 'id': friend_id }
    friends = mysql.query_db(query, data)
    return render_template('index.html', one_friend=friends[0])

@app.route('/friends', methods=['POST'])
def create():
    print request.form
    query = 'INSERT INTO friends(first_name, last_name, occupation, created_at, updated_at) VALUES(:first_name, :last_name, :occupation, now(), now())'
    data = {
        'first_name': request.form['first-name'],
        'last_name': request.form['last-name'],
        'occupation': request.form['occupation']
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/update_friend/<friend_id>')
def updat(friend_id):
    query = 'UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id'
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation'],
        'id': friend_id
        }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
    query = 'DELETE FROM friends WHERE id = :id'
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
