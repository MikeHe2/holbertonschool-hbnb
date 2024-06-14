from flask import Flask, request, jsonify
from Model import city  # from Main Model module

app = Flask(__name__)


@app.route('/city', methods=['POST'])
def post_city():
    data = request.get_json()
    city = City(data['id'], data['name'], data['description'])
    # save the city to the database
    # print city for now
    print(city)
    return jsonify(city.__dict__), 201  # return response


@app.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    # retrieve the city with the given id from database
    # Return City test for now
    city = City(city_id, "City Test")
    return jsonify(city.__dict__), 200  # return the city's data
