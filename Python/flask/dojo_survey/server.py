from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'csdavis09'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/post', methods=['POST'])
def create_user():
    print request.form
    if len(request.form['name']) < 1:
        flash('Please enter a valid name!')
    else:
        flash('Success! You entered: {}'.format(request.form['name']))
    if len(request.form['message']) < 1:
        flash('Please enter a valid comment!')
    elif len(request.form['message']) > 120:
        flash('Please keep comments to less than 120 characters!')
    else:
        flash('Thank you for your comments!')
    return redirect('/')
    session['name']= request.form['name']
    session['location'] = request.form['locations']
    session['favorite_language'] = request.form['language']
    session['comments'] = request.form['message']
    return redirect('/')
# @app.route('/process', methods=['POST'])
# def process():
#
@app.route('/result')
def post_user():
    return render_template('result.html')

app.run(debug=True)


# def go_back():
#     back = request.form['go-back']
#     return redirect('/')
# name=session['name'], locations=session['location'], favorite_language=session['favorite_language'], comments=session['comments']
