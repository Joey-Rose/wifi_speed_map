import redis
import json

r = redis.Redis(host='redis-13143.c289.us-west-1-2.ec2.cloud.redislabs.com', port=13143, db=0, password='v5pV7Uj9UPU0mEsTUCJz6tlg74SYAYch')

data = {
    'foo': 'bar'
}
geojson = {
            'type': 'FeatureCollection',
            'features': [
                {
                    'type': 'Feature',
                    'properties': {
                        'description':
                            'Download: 200 Mbps, Upload: 180 Mbps'
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
                    'properties': {
                        'description':
                            'Download: 2000 Mbps, Upload: 1800 Mbps'
                    },
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [-74.038659, 33.931567]
                    }
                }
# print(r.execute_command('KEYS *'))
# r.execute_command('JSON.SET', 'doc', '.', json.dumps(data))
# r.execute_command('JSON.SET', 'geojson', '.', json.dumps(geojson))
# r.execute_command('JSON.ARRAPPEND', 'geojson', '.features', json.dumps(new_user_input))
reply = json.loads(r.execute_command('JSON.GET', 'geojson'))

print(reply)