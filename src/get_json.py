# tutorial on how to deploy an AWS Lambda function as a .zip file: https://www.youtube.com/watch?v=rDbxCeTzw_k

import redis
import json
import os

r = redis.Redis(host=os.environ["REDIS_HOST"], port=13143, db=0, password=os.environ["REDIS_PWD"])

def get_json(event, context):
    reply = r.execute_command('JSON.GET', 'geojson')

    return {
        "statusCode": 200,
        "body": reply.decode("utf-8"),
        "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "*"}
    }