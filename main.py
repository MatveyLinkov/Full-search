import sys
import requests
from PIL import Image
from io import BytesIO
from params import get_spn

geocoder_api_server = 'http://geocode-maps.yandex.ru/1.x/'
toponym = ' '.join(sys.argv[1:])
geocoder_params = {
    'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
    'geocode': toponym,
    'format': 'json'
}

response = requests.get(geocoder_api_server, params=geocoder_params)

if response:
    json_response = response.json()
    toponym_ans = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    toponym_coord = toponym_ans['Point']['pos']
    toponym_lon, toponym_lat = toponym_coord.split()
    map_api_server = 'http://static-maps.yandex.ru/1.x/'
    map_params = {
        'll': f'{toponym_lon},{toponym_lat}',
        'spn': get_spn(toponym_ans),
        'l': 'map',
        'pt': f'{toponym_lon},{toponym_lat},pm2rdl'
    }
    response = requests.get(map_api_server, params=map_params)
    Image.open(BytesIO(response.content)).show()
