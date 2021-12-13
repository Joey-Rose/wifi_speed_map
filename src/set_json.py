# tutorial on how to deploy an AWS Lambda function as a .zip file: https://www.youtube.com/watch?v=rDbxCeTzw_k

import redis
import json
import jwt
import os

r = redis.Redis(host=os.environ["REDIS_HOST"], port=13143, db=0, password=os.environ["REDIS_PWD"])

def set_json(event, context):
    r.execute_command('JSON.ARRAPPEND', 'geojson', '.features', event['body'])
    body = json.loads(event['body'])
    token = jwt.encode({'last_location': str(body['geometry']['coordinates'][0]) + "," + str(body['geometry']['coordinates'][1])}, os.environ["SECRET_KEY"])
        
    return {
        "statusCode": 200,
        "body": json.dumps({"last_location": token}),
        "headers": {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "*"}
    }