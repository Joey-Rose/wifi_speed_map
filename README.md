wifi_speed_map

tippecanoe --force -r1 -e ./dynamic_data --layer=data --no-feature-limit --no-tile-size-limit dynamic_data.json
tippecanoe --force -r1 -e ./s3_tiles --layer=data --no-feature-limit --no-tile-size-limit old_data.json
tile-join --force -e merged_tiles dynamic_data s3_tiles

tippecanoe --minimum-zoom=0 --maximum-zoom=9 -e ./static/clustered_tiles_100000_points -r1  --cluster-distance=50 --accumulate-attribute=download:mean --layer=data --force ./static/100000_points.json

tippecanoe --minimum-zoom=10 --maximum-zoom=10 -e ./static/clustered_tiles_1000000_points -r1 --layer=data --allow-existing ./static/1000000_points.json


        - tippecanoe -z14 -e ./static/clustered_tiles_100000_points -r1 --simplification=10 --cluster-distance=50 --accumulate-attribute=download:mean --layer=data --force ./static/100000_points.json