#!/usr/bin/python3
"""Instance of Flask"""

from views import app_views
from flask import jsonify, request, abort
from models import storage
#from models.place import Place
#from models.base_model import BaseMode

@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_places_by_id(place_id):
    """Gets a places base form the id."""
    data_id = storage.get("Place", place_id)
    if data_id is None:
        abort(404)
    else:
        return jsonify(data_id.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_places_by_id(place_id):
    """Deletes a places base form the id."""
    data_id = storage.get(Place, place_id)
    if data_id is None:
        abort(404)
    storage.delete(data_id)
    storage.save()
    return jsonify({}), 200
  
@app_views.route('/places', methods=['POST'],
                 strict_slashes=False)
def create_a_places():
    """ Create a new places."""

@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def put_a_places(place_id):
    """ Update a old places."""
    first_place = storage.get("Place", place_id)
    if first_place is None:
        abort(404)
    is_json = request.get_json()
    if is_json is None:
        abort(400, "Not a JSON")
    dont = ['id', 'created_at', 'updated_at']
    for key, value in is_json.items():
        if key in dont:
            pass
        else:
            setattr(first_place, key, value)
    first_place.save()
    return jsonify(first_place.to_dict()), 200