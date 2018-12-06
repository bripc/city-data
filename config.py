import os

TREES_GEOJSON_URL = 'https://opendata.arcgis.com/datasets/b9b716e09b5048179ab648bb4518452b_0.geojson'

FLORA_URL = 'http://ucjeps.berkeley.edu/flora_index.html'
FLORA_A_TAG_IDENTIFIER = 'http://bscit.berkeley.edu/cgi-bin/display_page?'


dir_path, filename = os.path.split(os.path.realpath(__file__))
LOCAL_PATH = dir_path
LOCAL_DATA_PATH = dir_path + '/data/'
