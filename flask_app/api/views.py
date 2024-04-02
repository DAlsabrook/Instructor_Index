"""
Module to contain all views for api information
"""
from flask import jsonify
from . import api_views

@api_views.route('/status')
def api_endpoint():
    data = {"message": "Hello from API",
            "statusCode": "200"}
    return jsonify(data)
