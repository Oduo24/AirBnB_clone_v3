#!/usr/bin/python3
"""Index for the blueprint"""

from api.v1.views import app_views

@app_views.route('/status')
def status():
    """Returns the status of the api
    """
    return {"status": "OK"}
