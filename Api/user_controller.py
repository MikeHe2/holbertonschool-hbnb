from flask import Blueprint, request, jsonify
from Persistence.IPersistence import IPersistenceManager
from Persistence.data_manager import DataManager  # from Main Model module
from datetime import datetime
from Model.users import Users


user_controller = Blueprint('user_controller', __name__)
data = DataManager()


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

    '''if data.get_user_by_email(email):
        return jsonify({'error': 'Email already exists'}), 409'''

    '''now = datetime()
    user = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'created_at': now,
            'updated_at': now
            }'''
    user = Users(email, first_name, last_name)
    #  new_user = data.post_user(user)
    return jsonify(user.__dict__), 201  # return response


@user_controller.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Gets user id"""
    user = data.get_user_by_id(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.__dict__), 200  # return the user's data


@user_controller.route('/users', methods=['GET'])
def get_users():
    """Gets all users list"""
    users = data.get_all_users()
    if users is None:
        return jsonify({'error': 'No users found'}), 404
    return jsonify(
        [user.__dict__ for user in users]), 200  # return all users' data


@user_controller.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """Update user id"""
    data = request.get_json()
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if not email or not first_name or not last_name:
        return jsonify({'error': 'Missing required fields'}), 400

    if '@' not in email:  # Simple email validation
        return jsonify({'error': 'Invalid email format'}), 400

    if updated_user is None:
        return jsonify({'error': 'User not found'}), 404

    now = datetime()
    updated_user = {
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'created_at': now,
        'updated_at': now
        }
    updated_user = data.update_user(user_id, updated_user)

    return jsonify(updated_user.__dict__), 200  # return response


@user_controller.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Deletes user id"""
    user = data.delete_user_by_id(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'message': 'User deleted successfully'}), 200
