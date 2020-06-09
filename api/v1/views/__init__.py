#!/usr/bin/python3
"""Instance of Flask"""


from flask import Blueprint
app_views = Blueprint('api', __name__, url_prefix='/api/v1')
from ..views.index import *
from ..views.users import *
from ..views.places import *
