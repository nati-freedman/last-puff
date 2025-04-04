from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


# Routes for all users: homepage, about, login/logout
# Routes for logged in user: user dashboard, feed

# Home page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

# About page
@app.route('/about')
def about():
    return render_template('about.html', title='About')

# Login page
@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)