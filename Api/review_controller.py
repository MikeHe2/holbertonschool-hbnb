from flask import Blueprint, request, jsonify
from .models import Review  # from Main Model module
from .IPersistence import IPersistenceManager
from persistence.DataManager import DataManager


review_controller = Blueprint('review_controller', __name__)


@review_controller.route('/reviews', methods=['POST'])
def post_review():
    data = request.get_json()
    review = Review(content=data['content'])
    return jsonify(review.to_dict()), 201


@review_controller.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews]), 200


@review_controller.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.query.get(review_id)
    if review is None:
        return jsonify({"error": "Review not found"}), 404
    return jsonify(review.to_dict()), 200


@review_controller.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    review = Review.query.get(review_id)
    if review is None:
        return jsonify({"error": "Review not found"}), 404
    review.content = data.get('content', review.content)
    review.save()
    return jsonify(review.to_dict()), 200


@review_controller.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.query.get(review_id)
    if review is None:
        return jsonify({"error": "Review not found"}), 404
    review.delete()
    return jsonify({'message': 'Review deleted'}), 204
