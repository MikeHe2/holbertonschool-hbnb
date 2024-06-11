from flask import Flask
from .user_controller import user_controller
from .country_city_controller import country_city_controller



app = Flask(__name__)
app.register_blueprint(user_controller)
app.register_blueprint(country_city_controller)
