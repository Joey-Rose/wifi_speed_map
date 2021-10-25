import redis
import json
import random
import time
import threading
import requests



data = {
    'foo': 'bar'
}
geojson = {
            'type': 'FeatureCollection',
            'features': [
                {
                    'type': 'Feature',
                    'properties': {
                        "download": 190,
                        "upload": 890,
                        "date": "5/3/20"
                    },
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [-77.038659, 38.931567]
                    }
                }
            ]
        }

new_user_input = {
                    'type': 'Feature',
                    "properties": {
                        "download": 100,
                        "upload": 80,
                        "date": "5/3/20"
                    },
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [-74.038659, 33.931567]
                    }
                }
# print(r.execute_command('KEYS *'))
# r.execute_command('JSON.SET', 'doc', '.', json.dumps(data))
# r.execute_command('JSON.SET', 'json', '.', json.dumps(geojson))
# r.execute_command('JSON.ARRAPPEND', 'geojson', '.features', json.dumps(new_user_input))
# reply = json.loads(r.execute_command('JSON.GET', 'geojson'))

# print(reply)

def add_rand_test():
    download = random.randrange(1, 1001)
    upload = random.randrange(1, 1001)
    date = "5/3/20"
    # Latitudes range from -90 to 90, and longitudes range from -180 to 90? instead of 80
    lat = random.randrange(-90, 89) + round(random.random(), 6)
    long = random.randrange(-180, 89) + round(random.random(), 6)
    
    new_user_input = {'type': 'Feature',"properties": {"download": download,"upload": upload,"date": date, "point_count": 1},'geometry': {'type': 'Point','coordinates': [long, lat]}}

    # r.execute_command('JSON.ARRAPPEND', 'geojson', '.features', json.dumps(new_user_input))
    # requests.post("http://127.0.0.1:5001/set_json", data=json.dumps(new_user_input))
    geojson['features'].append(new_user_input)

start = time.time()
for i in range(1000000):
    # threading.Thread(target=add_rand_test, args=()).start()
    add_rand_test()
end = time.time()
print()
print(end-start, "many seconds passed")
# reply = r.execute_command('JSON.GET', 'geojson')
with open("./static/dynamic_data.json", "w") as f:
    f.write(json.dumps(geojson))