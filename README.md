wifi_speed_map

tippecanoe --force -r1 -e ./dynamic_data --layer=data --no-feature-limit --no-tile-size-limit dynamic_data.json
tippecanoe --force -r1 -e ./s3_tiles --layer=data --no-feature-limit --no-tile-size-limit old_data.json
    - Or just download s3 folder
tile-join --force -e merged_tiles dynamic_data s3_tiles