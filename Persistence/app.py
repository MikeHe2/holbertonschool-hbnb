from flask import Flask
from .user_controller import user_controller
from .country_city_controller import country_city_controller
from .amenity_controller import amenity_controller
from .place_controller import place_controller
from .review_controller import review_controller
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.register_blueprint(user_controller)
app.register_blueprint(country_city_controller)
app.register_blueprint(amenity_controller)
app.register_blueprint(place_controller)
app.register_blueprint(review_controller.py)

if __name__ == '__main__':
    app.run(host='localhost', port=8081, debug=True)
