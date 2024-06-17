from flask import Blueprint, request, jsonify
from Persistence.data_manager import DataManager  # from Main Model module
from datetime import datetime
from Model.users import User


user_controller = Blueprint('user_controller', __name__)
data_manager = DataManager()
users = User

@user_controller.route('/user', methods=['POST'])
def post_user():
    """Creates new user"""
    data = request.get_json()
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if not email or not first_name or not last_name:
        return jsonify({'error': 'Missing required fields'}), 400

    if '@' not in email:  # Simple email validation
        return jsonify({'error': 'Invalid email format'}), 400

    if User.email_exists(email):
        return jsonify({'error': 'Email already exists'}), 409

    user = User(email=email, first_name=first_name, last_name=last_name)
    data_manager.save(user)
    return jsonify(user.__dict__), 201


@user_controller.route('/user', methods=['GET'])
def get_users():
    """Gets all users list"""
    users = data_manager.get_all('User')
    return jsonify(users), 200

@user_controller.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    """Update user by id"""
    data = request.get_json()

    # Load existing user data
    existing_user_data = data_manager.get(user_id, 'User')
    if not existing_user_data:
        return jsonify({'error': 'User not found'}), 404

    # Check if email is provided and validate it
    email = data.get('email')
    if email:
        if '@' not in email:  # Simple email validation
            return jsonify({'error': 'Invalid email format'}), 400
        if email != existing_user_data['email'] and User.email_exists(email):
            return jsonify({'error': 'Email already exists'}), 409

    # Update user data
    existing_user_data['email'] = email or existing_user_data['email']
    existing_user_data['first_name'] = data.get('first_name', existing_user_data['first_name'])
    existing_user_data['last_name'] = data.get('last_name', existing_user_data['last_name'])

    # Create and update user without using **kwargs
    updated_user = User(
        email=existing_user_data['email'],
        first_name=existing_user_data['first_name'],
        last_name=existing_user_data['last_name']
    )
    updated_user.id = user_id  # Ensure the ID remains the same
    data_manager.update(updated_user)

    return jsonify(updated_user.__dict__), 200



@user_controller.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Deletes user id"""
    user = data_manager.get(entity_id=user_id, entity_type='User')
    if user is None:
        return jsonify({"error": "user not found"}), 404
    data_manager.delete(entity_id=user_id, entity_type='User')
    return jsonify({'message': 'User deleted'}), 204
