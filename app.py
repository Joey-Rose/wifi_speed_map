from flask import Flask, render_template, request, Response, redirect, make_response
import redis
import json
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234' # TODO: change this 

r = redis.Redis(host="redis-13143.c289.us-west-1-2.ec2.cloud.redislabs.com", port=13143, db=0, password="v5pV7Uj9UPU0mEsTUCJz6tlg74SYAYch")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_json')
def get_json():
    reply = r.execute_command('JSON.GET', 'geojson')

    resp = Response(
            reply.decode("utf-8"),
            status=200,
            mimetype='application/json'
        )
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/set_json', methods = ['POST', 'OPTIONS'])
def set_json():
    # resp = redirect("http://127.0.0.1:5001/tiled_way_orig")
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    # resp.headers['Access-Control-Allow-Headers'] = '*'
    resp = Response(status=200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = '*'
    if request.method == 'OPTIONS':
        return resp
    
    print("request is", request.data)
    payload = json.loads(request.data)
    print("payload is", payload)
    r.execute_command('JSON.ARRAPPEND', 'geojson', '.features', request.data)
    token = jwt.encode({'last_location': str(payload['geometry']['coordinates'][0]) + "," + str(payload['geometry']['coordinates'][1])}, app.config['SECRET_KEY'])
    
    # resp.set_cookie('last_location', token)
    resp.headers['Set-Cookie'] = 'last_location=' + token
    return resp

@app.route('/wipe_redis_data')
def wipe_redis_data():
    inital_data = {
        "type": "FeatureCollection",
        "features": []
    }
    
    reply = r.execute_command('JSON.SET', 'geojson', '.', json.dumps(inital_data))

    return reply

@app.route('/tiled_way_orig')
def tiled_way_orig():
    return render_template('tiled_way_orig.html')

@app.route('/authenticate')
def authenticate():
    return render_template('authenticate.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
