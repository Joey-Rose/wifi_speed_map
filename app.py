from flask import Flask, render_template, request, Response
import redis
import json

app = Flask(__name__)

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

@app.route('/set_json', methods = ['POST'])
def set_json():
    r.execute_command('JSON.ARRAPPEND', 'geojson', '.features', request.data)

@app.route('/mb2')
def mb2():
    return render_template('other_mapbox.html')

@app.route('/wipe_redis_data')
def wipe_redis_data():
    inital_data = {
        "type": "FeatureCollection",
        "features": []
    }
    
    reply = r.execute_command('JSON.SET', 'geojson', '.', json.dumps(inital_data))

    return reply

if __name__ == '__main__':
    app.run(debug=True, port=5001)
