#!/usr/bin/python3
"""Index for the blueprint"""

from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify

@app_views.route('/status', strict_slashes=False)
def status_of_api():
    """Returns the status of the api
    """
    return jsonify({"status": "OK"})
