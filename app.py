from flask import Flask
<<<<<<< HEAD
from Api.user_controller import user_controller
from Api import country_city_controller
from Api import amenity_controller
from Api import place_controller
from Api import review_controller

app = Flask(__name__)

app.register_blueprint(user_controller)
app.register_blueprint(country_city_controller)
app.register_blueprint(amenity_controller)
app.register_blueprint(place_controller)
app.register_blueprint(review_controller)


if __name__ == '__main__':
    app.run(host='localhost', port=8081, debug=True)


=======

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Hbnb part 1"

@app.route('/hello')
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
>>>>>>> d65af3c8315ac9b9d57aa81989ec47e03b5c8975
