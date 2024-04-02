"""
module used for user log in
"""
from flask import Flask, jsonify
from models import storage
from flask_app.api.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)

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

#
