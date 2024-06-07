#!/usr/bin/env python3

from flask import request, jsonify
from . import app, db
from .models import User, Place, Review, Amenity, Country, City

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    new_user = User(email=data['email'], first_name=data['first_name'], last_name=data['last_name'],password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201