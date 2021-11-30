wifi_speed_map

# Random notes I will delete later
tippecanoe --force -r1 -e ./dynamic_data --layer=data --no-feature-limit --no-tile-size-limit dynamic_data.json
tippecanoe --force -r1 -e ./s3_tiles --layer=data --no-feature-limit --no-tile-size-limit old_data.json
tile-join --force -e merged_tiles dynamic_data s3_tiles

tippecanoe --minimum-zoom=0 --maximum-zoom=9 -e ./static/clustered_tiles_100000_points -r1  --cluster-distance=50 --accumulate-attribute=download:mean --layer=data --force ./static/100000_points.json

tippecanoe --minimum-zoom=10 --maximum-zoom=10 -e ./static/clustered_tiles_1000000_points -r1 --layer=data --allow-existing ./static/1000000_points.json

Merging folders together:
Merging clusters: tippecanoe --minimum-zoom=0 --maximum-zoom=9 -e ./static/clustered_tiles_100_points -r1  --cluster-distance=75 --accumulate-attribute=download:mean --layer=data --force ./static/100000_points.json ./static/clustered_tiles_100_points

Adding points to archived layer: tippecanoe --minimum-zoom=10 --maximum-zoom=10 -e ./static/clustered_tiles_100_points -r1 --layer=data --allow-existing ./static/100000_points.json ./static/clustered_tiles_100_points

Just add another source and the processing takes place! Such processing does not take place with tile-join

# How to get setup
- cd into a folder of your choice
- git clone https://github.com/Joey-Rose/wifi_speed_map.git
- cd wifi_speed_map
- python3 -m venv venv
- . venv/bin/activate
- pip install -r requirements.txt
- python3 app.py
- navigate to http://127.0.0.1:5001/tiled_way_orig
- read privacy policy, click continue, and witness a point get added to a map with 1 million points