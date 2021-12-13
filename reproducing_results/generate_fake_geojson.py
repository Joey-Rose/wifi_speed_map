import json
import random
import time

geojson = {
            'type': 'FeatureCollection',
            'features': []
        }

def add_rand_test():
    download = random.randrange(1, 1001)
    upload = random.randrange(1, 1001)
    date = "5/3/20"
    
    # American longitudes range from -118 to -74, and latitudes range from 34 to 40? 
    lat = random.randrange(34, 40) + round(random.random(), 6)
    long = random.randrange(-118, -75) + round(random.random(), 6)
    
    new_user_input = {'type': 'Feature',"properties": {"download": download,"upload": upload,"date": date},'geometry': {'type': 'Point','coordinates': [long, lat]}}
    geojson['features'].append(new_user_input)

    # South American longitudes range from -52 to -69 and latitudes range from -1 to -39
    lat = random.randrange(-40, -1) + round(random.random(), 6)
    long = random.randrange(-70, -52) + round(random.random(), 6)
    
    new_user_input = {'type': 'Feature',"properties": {"download": download,"upload": upload,"date": date},'geometry': {'type': 'Point','coordinates': [long, lat]}}
    geojson['features'].append(new_user_input)

    # African longitudes range from 13 to 32 and latitudes range from 30 to -28
    lat = random.randrange(-28, 30) + round(random.random(), 6)
    long = random.randrange(13, 32) + round(random.random(), 6)
    
    new_user_input = {'type': 'Feature',"properties": {"download": download,"upload": upload,"date": date},'geometry': {'type': 'Point','coordinates': [long, lat]}}
    geojson['features'].append(new_user_input)

    # European and Asian longitudes range from -1 to 121 and latitudes range from 53 to 24
    lat = random.randrange(24, 53) + round(random.random(), 6)
    long = random.randrange(-1, 121) + round(random.random(), 6)
    
    new_user_input = {'type': 'Feature',"properties": {"download": download,"upload": upload,"date": date},'geometry': {'type': 'Point','coordinates': [long, lat]}}
    geojson['features'].append(new_user_input)

    # Austrailian longitudes range from 121 to 148 and latitudes range from -20 to -32
    lat = random.randrange(-32, -20) + round(random.random(), 6)
    long = random.randrange(121, 148) + round(random.random(), 6)
    
    new_user_input = {'type': 'Feature',"properties": {"download": download,"upload": upload,"date": date},'geometry': {'type': 'Point','coordinates': [long, lat]}}
    geojson['features'].append(new_user_input)
    
start = time.time()
for i in range(1000 // 5):
    add_rand_test()
end = time.time()
print()
print(end-start, "many seconds passed")
with open("./static/1000_points.json", "w") as f:
    f.write(json.dumps(geojson))