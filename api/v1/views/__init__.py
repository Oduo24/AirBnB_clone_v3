#!/usr/bin/python3
"""Initialize views package"""

from flask import Blueprint
from api.vi.views.index import *

app_views = Blueprint(url_prefix='/api/v1')

