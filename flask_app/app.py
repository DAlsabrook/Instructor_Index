"""
module used for user log in
"""
from flask import Flask, jsonify
from models import storage
from flask_login import LoginManager
from models.user import User
from flask_app.api import api_views
from flask_app.web import web_views


app = Flask(__name__, template_folder='../public', static_folder='../public/static')
app.register_blueprint(api_views)
app.register_blueprint(web_views)
app.secret_key = 'secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.errorhandler(404)
def handle_errors(error):
    """Handle 404 page with dict"""
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def close_storage(exception):
    """Call storage.close()"""
    storage.close()

if __name__ == '__main__':
    app.run(debug=True)
