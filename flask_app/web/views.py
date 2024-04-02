"""
module used for all views to serve html pages
"""
from flask import request, redirect, url_for, render_template
from flask_login import login_user, logout_user, login_required
from models import storage
from . import web_views


@web_views.route('/', strict_slashes=False)
def home():
    return render_template('index.html')


@web_views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        input_username = request.form['username']
        input_password = request.form['password']
        user = storage.user(input_username, input_password)
        if user:
            login_user(user)
            return redirect(url_for('web.home'))
        else:
            return 'Login Failed'
    return render_template('login.html')


@web_views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('web.home'))


@web_views.route('/signup', strict_slashes=False)
def signup():
    return render_template('signup.html')


@web_views.route('/schools', strict_slashes=False)
def schools():
    return render_template('school.html')


@web_views.route('/instructors', strict_slashes=False)
def instructors():
    return render_template('instructor.html')
