"""
Package module for views
"""
from flask import Blueprint

web_views = Blueprint('web', __name__)


from .views import *
