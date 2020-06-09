#!/usr/bin/python3
"""Instance of Flask"""


from ..views import app_views
from flask import Flask, jsonify


app = Flask(__name__)


@app_views.route("/status")
def json_status():
    """ Returns Dummy Text."""
    return jsonify(status='OK')


@app_views.route("/stats")
def count_classes():
    """
        method to return a jsonified dictionary of stats.
    """
    return jsonify({"places": storage.count("Place"),
                    "users": storage.count("User")})
