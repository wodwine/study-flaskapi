from flask_restful import Resource, abort

my_city = {
    "bkk": {"weather": "Good", "people": "8M"},
    "nst": {"weather": "Best", "people": "2M"},
    "phk": {"weather": "Bad", "people": "0.5M"},
}


def validate_request(city_name):
    if city_name not in my_city:
        abort(404, message=f"{city_name} not found")
    return True


class WeatherCity(Resource):
    @staticmethod
    def get(city_name):
        if validate_request(city_name):
            return {"response": {"city": city_name, "data": my_city[city_name]}}

    @staticmethod
    def post(city_name):
        return {"response": f"Data Weather Post of {city_name}"}
