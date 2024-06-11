from flask import Flask, request, jsonify
from .models import Country  # from Main Model module

app = Flask(__name__)


@app.route('/country', methods=['POST'])
def post_country():
    data = request.get_json()
    country = Country(data['id'], data['name'], data['description'])
    # save the country to the database
    # print country for now
    print(country)
    return jsonify(country.__dict__), 201  # return response


@app.route('/countries/<country_id>', methods=['GET'])
def get_country(country_id):
    # retrieve the country with the given id from database
    # Return Country test for now
    country = Country(country_id, "Country Test")
    return jsonify(country.__dict__), 200  # return the country's data
