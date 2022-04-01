from flask_restful import Resource


class WeatherCity(Resource):
    def get(self):
        return {"data": "Hello Weather City in Thailand"}
