"""
module used for user log in
"""
from flask import Flask, request, redirect, url_for, render_template
from models import storage


app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
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

if __name__ == '__main__':
    app.run(debug=True)
