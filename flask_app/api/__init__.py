"""
Package module for views
"""
from flask import Blueprint

api_views = Blueprint('api', __name__, url_prefix='/api')


from .views import *
