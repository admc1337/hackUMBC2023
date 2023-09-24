from flask import render_template, url_for, flash, redirect
from weatherapp import app
from weatherapp.forms import RegistrationForm, LoginForm, myForm

app.config['SECRET_KEY'] = 'd5c919d9ca2cc6d410ba11b8070f7314'
posts = [
    {
        'author': 'Username',
        'title': 'Area in Zip Code',
        'content': 'Current Weather'
    },
    {
        'author': 'Username',
        'title': 'Movie Recommendation',
        'content': 'Synopsis, Year, etc'
    }
]

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = myForm()
    if form.validate_on_submit():
        flash(f'Zip Code at {form.zipcode.data} Found.', 'success')
        return redirect(url_for('results'))    
    return render_template('home.html', title='Home', form=form)
    #return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/results")
def results():
    return render_template('results.html', title='Results')

@app.route("/error")
def error():
    return render_template('error.html', title='Page Error')
    
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}.', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@weather.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
    