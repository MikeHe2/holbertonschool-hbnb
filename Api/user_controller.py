from flask import Flask, request, jsonify
from .models import User  # from Main Model module

app = Flask(__name__)


@app.route('/user', methods=['POST'])
def post_user():
    data = request.get_json()
    user = User(data['id'], data['first_name'], data['last_name'],
                data['email'], data['password'])
    # save the user to the database
    # print user for now
    print(user)
    return jsonify(user.__dict__), 201  # return response


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    # retrieve the user with the given id from database
    # Return User test for now
    user = User(user_id, "User Test")
    return jsonify(user.__dict__), 200  # return the user's data
