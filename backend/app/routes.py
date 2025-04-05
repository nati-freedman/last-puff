from urllib.parse import urlsplit

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import app, db
from app.forms import LoginForm
from app.models import User

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
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('logim'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page=url_for('user_dashboard')
        return redirect(next_page)
    return render_template('login.html', title='Login', form=form)

# Logout user and redirect to the home page
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# User dashboard page
# TODO: CUSTOM URL
@app.route('/dashboard')
@login_required
def user_dashboard():
    return render_template('dashboard.html', title='Dashboard')

# User feed page
# TODO: CUSTOM URL
@app.route('/feed')
@login_required
def user_feed():
    return render_template('feed.html', title='Feed')