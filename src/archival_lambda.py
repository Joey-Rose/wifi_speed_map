import json, os
import requests
import redis
from subprocess import run

def handler(event, context):
    # write redis json to disk
    redis_conn = redis.Redis(host=os.environ["REDIS_HOST"], port=13143, db=0, password=os.environ["REDIS_PWD"])
    reply = redis_conn.execute_command('JSON.GET', 'geojson')
    with open("/tmp/dynamic_data.json", "w") as f:
        f.write(reply.decode("utf-8"))

    # download the S3 folder
    cmd = ['mkdir /tmp/s3_files && aws s3 sync s3://www.wifimap.live /tmp/s3_tiles']
    r = run(cmd, capture_output=True, shell=True)

    # merge the two datasets into to a third folder
    # for the first 10 zoom levels, only cluster the data: do not include any individual points
    cmd = ['mkdir /tmp/merged_tiles && tippecanoe --minimum-zoom=0 --maximum-zoom=9 -e ./tmp/merged_tiles -r1  --cluster-distance=75 --accumulate-attribute=download:mean --layer=data --force ./tmp/dynamic_data.json ./tmp/s3_tiles']
    r = run(cmd, capture_output=True, shell=True)

    # for the 10th zoom level, do not do any clustering: just overlap individual points at this zoom level
    cmd = ['tippecanoe --minimum-zoom=10 --maximum-zoom=10 -e ./tmp/merged_tiles -r1 --layer=data --allow-existing ./tmp/dynamic_data.json ./tmp/s3_tiles']
    r = run(cmd, capture_output=True, shell=True)

    # replace S3 bucket with new folder
    cmd = ['aws s3 rm s3://www.wifimap.live --recursive']
    r = run(cmd, capture_output=True, shell=True)

    cmd = ['aws s3 sync /tmp/merged_tiles/ s3://www.wifimap.live --content-encoding gzip']
    r = run(cmd, capture_output=True, shell=True)
    
    # reset the json in Redis
    inital_data = {
        "type": "FeatureCollection",
        "features": []
    }
    reply = redis_conn.execute_command('JSON.SET', 'geojson', '.', json.dumps(inital_data))
    
    return {
        'headers': {'Content-Type' : 'application/json'},
        'statusCode': 200
    }