#!/usr/bin/python3
"""Instance of Flask"""


from flask import Flask, jsonify, request, abort
from models import storage, user
from api.v1.views import app_views
from models.user import User


@app_views.route('/users', methods=['GET'],
                 strict_slashes=False)
def get_users():
    """Gets all user by id"""
    new_dict = []
    for data in storage.all("User").values():
        new_dict.append(data.to_dict())
    return jsonify(new_dict)


@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def get_user_by_id(user_id=None):
    """Gets a user base form the id."""
    data_id = storage.get("User", user_id)
    if data_id is None:
        abort(404)
    else:
        return jsonify(data_id.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user_by_id(user_id=None):
    """Deletes a user base form the id."""
    data_id = storage.get("User", user_id)
    if data_id is None:
        abort(404)
    else:
        storage.delete(data_id)
        storage.save()
        return jsonify({}), 200


@app_views.route('/users', methods=['POST'],
                 strict_slashes=False)
def create_a_user():
    """ Create a new user."""
    is_json = request.get_json(silent=True)
    if is_json is None:
        abort(400, "Not a JSON")
    if 'email' not in is_json:
        abort(400, 'Missing email')
    if 'password' not in is_json:
        abort(400, 'Missing password')
    new_user = User(**is_json)
    new_user.save()
    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'],
                 strict_slashes=False)
def put_a_user(user_id):
    """ Update a old user."""
    first_user = storage.get("User", user_id)
    if first_user is None:
        abort(404)
    is_json = request.get_json()
    if is_json is None:
        abort(400, "Not a JSON")
    dont = ['id', 'email', 'created_at', 'updated_at']
    for key, value in is_json.items():
        if key in dont:
            pass
        else:
            setattr(first_user, key, value)
    first_user.save()
    return jsonify(first_user.to_dict()), 200
