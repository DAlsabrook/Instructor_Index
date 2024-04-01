"""
Package module for views
"""
from flask import Blueprint

app_views = Blueprint('api', __name__, url_prefix='/api')


from api.views.login import *

