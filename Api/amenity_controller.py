from flask import Blueprint, request, jsonify
from Model.amenities import Amenities # from Main Model module
from Persistence.data_manager import DataManager


amenity_controller = Blueprint('amenity_controller', __name__)
data_manager = DataManager()


@amenity_controller.route('/amenities', methods=['POST'])
def post_amenity():
    data = request.get_json()
    amenity = Amenities(name=data['name'], description=data['description'])
    data_manager.save(amenity)
    return jsonify(amenity.__dict__), 201


@amenity_controller.route('/amenities', methods=['GET'])
def get_amenities():
    data = data_manager._load_data()
    data_manager.get(entity_type=type(Amenities))
    return jsonify(data), 200


@amenity_controller.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = data_manager.get(entity_id=amenity_id, entity_type='Amenities')
    if amenity is None:
        return jsonify({"error": "Amenity not found"}), 404
    return jsonify(amenity), 200


@amenity_controller.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.get_json()
    existing_amenity = data_manager.get(entity_id=amenity_id, entity_type='Amenities')
    if existing_amenity is None:
        return jsonify({"error": "Amenity not found"}), 404

    updated_name = data.get('name', existing_amenity.get('name'))
    updated_description = data.get('description', existing_amenity.get('description'))

    updated_amenity = Amenities(name=updated_name, description=updated_description)
    updated_amenity.id = amenity_id  # Preserve the original ID
    data_manager.update(updated_amenity)
    return jsonify(updated_amenity.__dict__), 200



@amenity_controller.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    existing_amenity = data_manager.get(entity_id=amenity_id, entity_type='Amenities')
    if existing_amenity is None:
        return jsonify({"error": "Amenity not found"}), 404
    data_manager.delete(entity_id=amenity_id, entity_type='Amenities')
    return jsonify({'message': 'Amenity deleted'}), 204
