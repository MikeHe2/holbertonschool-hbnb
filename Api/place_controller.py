from flask import Blueprint, request, jsonify
from Model.place import Place  # from Main Model module
from Persistence.data_manager import DataManager


place_controller = Blueprint('place_controller', __name__)


@place_controller.route('/places', methods=['POST'])
def post_place():
    data = request.get_json()
    place = Place(name=data['name'])
    return jsonify(place.to_dict()), 201


@place_controller.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    place = Place.query.get(place_id)
    if place is None:
        return jsonify({"error": "Place not found"}), 404
    return jsonify(place.to_dict()), 200


@place_controller.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.get_json()
    place = Place.query.get(place_id)
    if place is None:
        return jsonify({"error": "Place not found"}), 404
    place.name = data.get('name', place.name)
    place.save()
    return jsonify(place.to_dict()), 200


@place_controller.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = Place.query.get(place_id)
    if place is None:
        return jsonify({"error": "Place not found"}), 404
    place.delete()
    return jsonify({'message': 'Place deleted'}), 204
