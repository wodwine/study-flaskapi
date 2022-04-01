from flask_restful import Resource

my_city = {
    "bkk": {"weather": "Good", "people": "8M"},
    "nst": {"weather": "Best", "people": "2M"},
    "phk": {"weather": "Bad", "people": "0.5M"},
}


class WeatherCity(Resource):
    @staticmethod
    def get(name):
        return {"response": {"province":name,"data":my_city[name]}}

    @staticmethod
    def post(name):
        return {"data": f"Data Weather Post of {name}"}
