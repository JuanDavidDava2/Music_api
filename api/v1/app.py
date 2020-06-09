#!/usr/bin/python3
"""Instance of Flask"""

from flask import Flask, jsonify, make_response
from .views import app_views
from os import getenv
from flask_cors import CORS


app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """Closes storage session"""
    storage.close()


@app.errorhandler(404)
def json_formatted_page_404_not_found(error):
    """Returns JSON 404 error."""
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)
    app.run(host=host, port=int(port), threaded=True)
