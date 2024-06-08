from flask import Flask, request, jsonify
from .models import Review  # from Main Model module

app = Flask(__name__)


@app.route('/review', methods=['POST'])
def post_review():
    data = request.get_json()
    review = Review(data['id'], data['name'], data['description'])
    # save the review to the database
    # print review for now
    print(review)
    return jsonify(review.__dict__), 201  # return response


@app.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    # retrieve the review with the given id from database
    # Return Review test for now
    review = Review(review_id, "Review Test")
    return jsonify(review.__dict__), 200  # return the review's data
