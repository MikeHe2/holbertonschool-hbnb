from flask import Blueprint, request, jsonify
from ..Model import Reviews  # from Main Model module
from ..Persistence import IPersistenceManager
from ..Persistence.data_manager import DataManager


review_controller = Blueprint('review_controller', __name__)


@review_controller.route('/reviews', methods=['POST'])
def post_review():
    data = request.get_json()
    review = Reviews(content=data['content'])
    return jsonify(review.to_dict()), 201


@review_controller.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Reviews.query.all()
    return jsonify([review.to_dict() for review in reviews]), 200


@review_controller.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    review = Reviews.query.get(review_id)
    if review is None:
        return jsonify({"error": "Review not found"}), 404
    return jsonify(review.to_dict()), 200


@review_controller.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    review = Reviews.query.get(review_id)
    if review is None:
        return jsonify({"error": "Review not found"}), 404
    review.content = data.get('content', review.content)
    review.save()
    return jsonify(review.to_dict()), 200


@review_controller.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Reviews.query.get(review_id)
    if review is None:
        return jsonify({"error": "Review not found"}), 404
    review.delete()
    return jsonify({'message': 'Review deleted'}), 204
