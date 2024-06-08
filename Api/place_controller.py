from flask import Flask, request, jsonify
from .models import Place  # from Main Model module

app = Flask(__name__)


@app.route('/place', methods=['POST'])
def post_place():
    data = request.get_json()
    place = Place(data['id'], data['name'], data['description'])
    # save the place to the database
    # print place for now
    print(place)
    return jsonify(place.__dict__), 201  # return response


@app.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    # retrieve the place with the given id from database
    # Return Place test for now
    place = Place(place_id, "Place Test")
    return jsonify(place.__dict__), 200  # return the place's data
