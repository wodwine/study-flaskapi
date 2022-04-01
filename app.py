from flask import Flask
from flask_restful import Api
from weather_city import WeatherCity

app = Flask(__name__)
api = Api(app)

api.add_resource(WeatherCity, "/weather/<string:name>")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
