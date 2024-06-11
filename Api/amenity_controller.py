from flask import Flask, request, jsonify
from .models import Amenity  # from Main Model module

app = Flask(__name__)


@app.route('/amenity', methods=['POST'])
def post_amenity():
    data = request.get_json()
    amenity = Amenity(data['id'], data['name'], data['description'])
    # save the amenity to the database
    # print amenity for now
    print(amenity)
    return jsonify(amenity.__dict__), 201  # return response


@app.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    # retrieve the amenity with the given id from database
    # Return Amenity test for now
    amenity = Amenity(amenity_id, "Amenity Test")
    return jsonify(amenity.__dict__), 200  # return the amenitie's data
