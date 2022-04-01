import requests

URL = "http://127.0.0.1:5000/weather/nst"
response = requests.get(URL)
print(response)
print(response.json())
