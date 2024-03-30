#!/usr/bin/python3

from models.state import State
from flask import jsonify, request, abort, make_response
from api.v1.views import app_views
from models import storage

@app_views.route("/states", methods = ['GET'])
def states_all():
    """"Returns list of all states"""
    states_all = []
    for state in storage.all("State").values:
        states_all.append(state.to_dict())
    return jsonify(states_all)

@app_views.route("/states/<state_id>", methods = ['GET'])
def state_get(state_id):
    """Handles get"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())
    
@app_views.route("states/<state_id>", method = ['DELETE'])
def state_delete(state_id):
    """"Deletes state"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200

@app_views.route("/states", method = ['POST'])
def post_state():
    """create a new state"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    state = State(**request.get_json())
    state.save()
    return make_response(jsonify(state.to_dict()), 201)




    

