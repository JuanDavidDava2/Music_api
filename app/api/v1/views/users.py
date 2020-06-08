from views import app_views
from flask import jsonify, request, abort


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
    
