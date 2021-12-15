# Code overview
The code for this project is split between two directories: /src/ and /reproducing_results/. The /reproducing_results/ directory contains all files necessary to replicate the evaluations performed on the three different map architectures. The files within it, along with their purpose, are defined below.

## /reproducing_results/
- clustered_tiles_1000000_points.zip
    - A compressed version of a /z/x/y directory of vector tiles collectively containing one million data points. It allows the reader to host an example archival layer on AWS S3 quicker as they do not have to generate it themselves
- generate_fake_geojson.py
    - A Python file that allows for the creation of a mock geospatial data points within a .json file adhering to the GeoJSON format. The reader can specify a certain number of data points to generate, and they will be generated across five different regions of the world
- get_json_lambda.zip
    - A .zip file containing all the information needed to deploy the /get_json microservice as an AWS Lambda function
- set_json_lambda.zip
    - A .zip file containing all the information needed to deploy the /set_json microservice as an AWS Lambda function
- on_the_fly_map.html
    - An HTML file containing an implementation of the on the fly map architecture. It fetches a .json payload from a Redis database hosted by RedisLabs to power the real-time layer. It does not include the authentication logic included in /src/map.html
- proposed_map.html
    - An HTML file containing an implementation of the on the fly map architecture. It fetches a .json payload from a Redis database hosted by RedisLabs to power the real-time layer and several .pbf files from an AWS S3 bucket to power the archival layer. It does not include the authentication logic included in /src/map.html
- pregeneration_map.html
    - An HTML file containing an implementation of the on the fly map architecture. It fetches several .pbf files from an AWS S3 bucket to power the archival layer. It does not include the authentication logic included in /src/map.html
- s3-cors.json
    - A .json file containing a preset configuration that prevents clients from receiving CORS errors when attempting to fetch files from the AWS S3 bucket created
- s3-policy.json
    - A .json file containing a preset configuration that tells an AWS S3 bucket what operations users can perform on the bucket. The “Resource” field must be changed by the reader to the ARN of their bucket when reproducing results

In addition to the /reproducing_results/ directory, the /src/ directory contains all files that make up an example implementation of the proposed architecture. It does not contain .zip files or Docker images ready to deploy services, but rather the programs that make up the identity of the Wi-Fi map application.The files within it, along with their purpose, are defined below.

##  /src/
- get_json.py
    - A Python file containing the code that makes up the /get_json microservice. It fetches the .json payload from Redis and returns it to the client
- set_json.py
    - A Python file containing the code that makes up the /set_json microservice. It adds a data point to the real-time layer data source living in a Redis database hosted via RedisLabs
- map.html
    - An HTML file containing an implementation of the on the fly map architecture. It fetches a .json payload from a Redis database hosted by RedisLabs to power the real-time layer and several .pbf files from an AWS S3 bucket to power the archival layer. The only difference between this file and /reproducing_results/proposed_map.html is that this file includes logic that verifies if a user has added a data point to the map before allowing them to view it. If they have, it centers the map on their last location.
- authentication.html
    - An HTML file that allows users to perform a Wi-fi speed test, have it uploaded to the real-time data source via the /set_json microservice, and redirects them to the map at their current location
- archival_lambda.py
    - A Python file containing the code that merges the real-time data source into the archival data source and then empties the data within the real time data source
- Dockerfile
    - A file that packages archival_lambda.py and its dependencies into a Docker image able to be deployed as an AWS Lambda function
- archival_lambda_requirements.txt
    - A .txt file containing a list of Python dependencies used by archival_lambda.py. It is used by the Dockerfile script to package these dependencies into the Docker image
