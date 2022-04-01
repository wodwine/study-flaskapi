from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_restful import Resource, abort, reqparse, marshal_with, fields

# App Server
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///weather.db"

# Mock data
my_city = {
    "bkk": {"weather": "Good", "people": "8M"},
    "nst": {"weather": "Best", "people": "2M"},
    "phk": {"weather": "Bad", "people": "0.5M"},
}

# Database
db = SQLAlchemy(app)

# API
api = Api(app)


class CityModel(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    temp = Column(Integer, nullable=False)
    weather = Column(String(100), nullable=False)
    people = Column(Integer, nullable=False)

    def __repr__(self):
        return f"CityModel({self.id},{self.name},{self.temp},{self.weather},{self.people})"


db.create_all()

city_add_args = reqparse.RequestParser()
city_add_args.add_argument("name", type=str, required=True, help="The name of the city must be string")
city_add_args.add_argument("temp", type=int, required=True, help="The value of the temp must be integer")
city_add_args.add_argument("weather", type=str, required=True, help="The value of the weather must be string")
city_add_args.add_argument("people", type=int, required=True, help="The number of people must be integer")

resource_field = {
    "id": fields.Integer,
    "name": fields.String,
    "temp": fields.Integer,
    "weather": fields.String,
    "people": fields.Integer,
}


# Model
class WeatherCity(Resource):

    @staticmethod
    @marshal_with(resource_field)
    def get(city_id):
        result = CityModel.query.filter_by(id=city_id).first()
        if not result:
            abort(404, message=f"{city_id} not found")
        return result

    @staticmethod
    @marshal_with(resource_field)
    def post(city_id):
        args = city_add_args.parse_args()
        city = CityModel(id=city_id, name=args["name"], temp=args["temp"],
                         weather=args["weather"], people=args["people"])
        db.session.add(city)
        db.session.commit()
        return city, 201


# Call
api.add_resource(WeatherCity, "/weather/<int:city_id>")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
