from flask import Flask, redirect, render_template, request, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'email_validation_db')
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app.secret_key = 'csdavis09'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/post', methods=['POST'])
def postEmailInfo():
    print request.form
    valid_form = True
    if not EMAIL_REGEX.match(request.form['email']):
        print 'REGEX does not match'
        flash('Please enter a valid email address')
        valid_form = False

    if valid_form == True:
        session['email'] = request.form['email']
        query = 'INSERT INTO users(email, created_at) VALUES(:email, now())'
        data = {
            'email': request.form['email']
        }
        mysql.query_db(query, data)
        idQuery = 'SELECT id FROM users WHERE email = :email' # Can set LIMIT to 1 to ensure that duplicates of the same email are not selected.
        user = mysql.query_db(idQuery, data)
        # uID = user[0]['id'] to create a separate userID page for each user
        # return redirect('/success/' + str(uID))
        return redirect('/success')
    else:
        return redirect('/')
@app.route('/success') #to select a single user, pass ('success/<userID>')
def displayEmailInfo(): #must pass userID to select single user
    query = 'SELECT * FROM users' # WHERE id = :id'
    # data = {
    #
    #     # 'email': email_address,
    #     # 'created': created
    # }
    email_list = mysql.query_db(query)
    flash('The email address you entered {}'.format(session['email']) + ' is a valid email. Success!')
    return render_template('success.html', email_list=email_list)
@app.route('/<email>', methods=['POST'])
def deleteEmail(email):
    print request.form
    valid_email = True
    session['email'] = request.form['email']
    if not EMAIL_REGEX.match(request.form['email']):
        print 'REGEX does not match'
        flash('Please enter a valid email address')
        valid_email = False
    if valid_email == True:
        query = 'DELETE FROM users WHERE email = :email'
        data = {'email': email}
        mysql.query_db(query, data)
        flash('You have successfully deleted the email address')
    return redirect('/')
# @app.route('/<id>', methods=["POST"])
# def destroy(id):
#     query = queries['delete']
#     data = {
#         'id' : id
#     }
#     flash('Successfully deleted email!')
#     mysql.query_db(query, data)
#     return redirect('/success')

app.run(debug=True)
