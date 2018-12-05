import os

TREES_GEOJSON_URL = 'https://opendata.arcgis.com/datasets/b9b716e09b5048179ab648bb4518452b_0.geojson'

dir_path, filename = os.path.split(os.path.realpath(__file__))
LOCAL_PATH = dir_path
LOCAL_DATA_PATH = dir_path + '/data/'
