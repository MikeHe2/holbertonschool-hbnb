from flask import Blueprint, request, jsonify
from ..Model import Amenities # from Main Model module
from ..Persistence import IPersistenceManager
from ..Persistence.data_manager import DataManager


amenity_controller = Blueprint('amenity_controller')
data = DataManager()


@amenity_controller.route('/amenities', methods=['POST'])
def post_amenity():
    data = request.get_json()
    amenity = Amenity(name=data['name'])
    return jsonify(amenity.to_dict()), 201


@amenity_controller.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = Amenity.query.all()
    return jsonify([amenity.to_dict() for amenity in amenities]), 200


@amenity_controller.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = Amenity.query.get(amenity_id)
    if amenity is None:
        return jsonify({"error": "Amenity not found"}), 404
    return jsonify(amenity.to_dict()), 200


@amenity_controller.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.get_json()
    amenity = Amenity.query.get(amenity_id)
    if amenity is None:
        return jsonify({"error": "Amenity not found"}), 404
    amenity.name = data.get('name', amenity.name)
    amenity.save()
    return jsonify(amenity.to_dict()), 200


@amenity_controller.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    amenity = Amenity.query.get(amenity_id)
    if amenity is None:
        return jsonify({"error": "Amenity not found"}), 404
    amenity.delete()
    return jsonify({'message': 'Amenity deleted'}), 204
