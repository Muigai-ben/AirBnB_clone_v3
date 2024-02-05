#!/usr/bin/python3
"""
Contains the blueprint for the API
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.amenities import *
from api.v1.views.cities import *
from api.v1.views.states import *
<<<<<<< HEAD
from api.v1.views.cities import *
from api.v1.views.amenities import *
=======
from api.v1.views.index import *
>>>>>>> 916278987c8e95b783a5ac781038bea180e13b7a
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.places_amenities import *
