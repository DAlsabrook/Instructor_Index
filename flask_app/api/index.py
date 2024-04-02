#!/usr/bin/python3
"""
Module to contain routes
"""
from api.views import app_views
from flask import render_template

@app_views.route('/')
def home():
    render_template('index.html')
@app_views.route('/status')
def status_json():
    """Return the status 'OK' if working"""
    status = {}
    status["status"] = "OK"
    return status
