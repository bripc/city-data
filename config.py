# lib imports
import os

# City of Sacramento API
TREES_GEOJSON_URL = 'https://opendata.arcgis.com/datasets/b9b716e09b5048179ab648bb4518452b_0.geojson'

# UC Berkeley's flora database HTML page
FLORA_URL = 'http://ucjeps.berkeley.edu/flora_index.html'
# use this to determine what should be used as a scientific name while scraping the web page
FLORA_A_TAG_IDENTIFIER = 'http://bscit.berkeley.edu/cgi-bin/display_page?'

# shortcut local paths
dir_path, filename = os.path.split(os.path.realpath(__file__))
LOCAL_PATH = dir_path
LOCAL_DATA_PATH = dir_path + '/data/'
