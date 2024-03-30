#!/usr/bin/python3

from api.v1.views import app_views
from models import storage


@app_views.route("/status")
def status():
    """"Returns status"""
    status = {"status": "OK"}
    return jsonify(status)

@app_views.route("/api/v1/stats")
def count():
    """ returns number of each objects by type """
    total = {}
    classes = {"Amenity": "amenities",
               "City": "cities",
               "Place": "places",
               "Review": "reviews",
               "State": "states",
               "User": "users"}
    for cls in classes:
        count = storage.count(cls)
        total[classes.get(cls)] = count
    return jsonify(total)