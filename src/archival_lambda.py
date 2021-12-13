import json, os
import requests
import redis
from subprocess import run

def handler(event, context):
    print("current directory is", os.getcwd())
    # write redis json to disk
    redis_conn = redis.Redis(host=os.environ["REDIS_HOST"], port=13143, db=0, password=os.environ["REDIS_PWD"])
    reply = redis_conn.execute_command('JSON.GET', 'geojson')
    with open("/tmp/dynamic_data.json", "w") as f:
        f.write(reply.decode("utf-8"))
    
    # convert dynamic_data.json to a folder
    cmd = ['tippecanoe --force -r1 -e /tmp/dynamic_data --layer=data --no-feature-limit --no-tile-size-limit /tmp/dynamic_data.json']
    # cmd = ['cat /tmp/dynamic_data.json']
    r = run(cmd, capture_output=True, shell=True)
    print("FIRST!!!!!", r.stderr)

    # download the S3 folder
    cmd = ['mkdir /tmp/s3_files && aws s3 sync s3://user-data-tiles /tmp/s3_tiles']
    r = run(cmd, capture_output=True, shell=True)
    print("SECOND!!!!", r.stderr)

    # merge the two folders to a third folder
    cmd = ['mkdir /tmp/merged_tiles && tile-join --force -e /tmp/merged_tiles /tmp/dynamic_data /tmp/s3_tiles']
    r = run(cmd, capture_output=True, shell=True)
    print("THIRD!!!!!", r.stderr)

    # replace S3 bucket with new folder
    cmd = ['aws s3 rm s3://user-data-tiles --recursive']
    r = run(cmd, capture_output=True, shell=True)
    print("FOURTH!!!!!", r.stderr)

    cmd = ['aws s3 sync /tmp/merged_tiles/ s3://user-data-tiles --content-encoding gzip']
    r = run(cmd, capture_output=True, shell=True)
    print("FIFTH!!!!!", r.stderr)
    
    # reset the json in Redis
    inital_data = {
        "type": "FeatureCollection",
        "features": []
    }
    reply = redis_conn.execute_command('JSON.SET', 'geojson', '.', json.dumps(inital_data))
    print("SIXTH!!!!!", reply)
    
    return {
        'headers': {'Content-Type' : 'application/json'},
        'statusCode': 200,
        'body': json.dumps({"message": "hello world",
                            "event": event})
    }