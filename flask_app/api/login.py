"""
module used for user log in
"""
from flask import request, render_template
from models import storage
from api.views import app_views

@app_views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        input_username = request.form['username']
        input_password = request.form['password']
        user = storage.user(input_username, input_password)
        if user:
            return render_template('index.html')
        else:
            return 'Login Failed'
    else:
        return render_template('log-in.html')
