from flask import Flask
from ..Api import user_controller
from ..Api import country_city_controller
from ..Api import amenity_controller
from ..Api import place_controller
from ..Api import review_controller

app = Flask(__name__)
app.register_blueprint(user_controller)
app.register_blueprint(country_city_controller)
app.register_blueprint(amenity_controller)
app.register_blueprint(place_controller)
app.register_blueprint(review_controller)
