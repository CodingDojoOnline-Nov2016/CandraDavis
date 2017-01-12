from flask import Flask, redirect, render_template, request, session, flash
app = Flask(__name__)
app.secret_key = 'csdavis09'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/find_ninja', methods=['POST'])
def find_ninja():
    print request.form
    return redirect('/ninja')
@app.route('/ninja')
def all_ninjas():
    return render_template('ninja.html')
@app.route('/ninja_select', methods=['POST'])
def select_by_color():
    print request.form
    validation = True
    if len(request.form['ninja_color']) < 1:
        flash('Please enter a valid color: red, blue, purple or orange')
        validation = False
    elif not unicode.isalpha(request.form['ninja_color']):
        validation = False
    if validation == False:
        return redirect('/401')
    else:
        session['color'] = request.form['ninja_color']
        return redirect('/ninja/'+ request.form['ninja_color'])
@app.route('/ninja/<ninja_color>')
def show_which_ninja(ninja_color):
    if session['color'] == 'blue' or session['color'] == 'Blue':
        return render_template('ninja_color.html', ninja_color=ninja_color)
    elif session['color'] == 'orange' or session['color'] == 'Orange':
        return render_template('ninja_color.html', ninja_color=ninja_color)
    elif session['color'] == 'red' or session['color'] == 'Red':
        return render_template('ninja_color.html', ninja_color=ninja_color)
    elif session['color'] == 'purple' or session['color'] == 'Purple':
        return render_template('ninja_color.html', ninja_color=ninja_color)
    else:
        return redirect('/401')
@app.route('/401')
def not_april():
    return render_template('exception401.html')
app.run(debug=True)
