import requests
from pprint import pprint
import json


pprint(dict(json.loads(requests.get("https://api.openweathermap.org/data/2.5/weather?lat=55.751244&lon=37.618423&appid=594156179360808d788f634d8738d7a8&lang=ru").content.decode('utf8'))))
