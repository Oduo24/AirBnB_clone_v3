#!/usr/bin/python3
"""Index for the blueprint"""

from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage

object_types = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
        }

@app_views.route('/status', strict_slashes=False)
def status_of_api():
    """Returns the status of the api
    """
    return jsonify({"status": "OK"})

@app_views.route('/stats', strict_slashes=False)
def stats():
    """Returns the number of each object by type
    """
    return_dict = {}
    for k,v in object_types.items():
        no_of_objects = storage.count(v)
        return_dict[k] = no_of_objects
    return jsonify(return_dict)
    
    
