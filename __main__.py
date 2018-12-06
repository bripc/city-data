import argparse
import json
import re
from bs4 import BeautifulSoup

# local imports
import config
import util
import tree

# global vars
tree_file = config.LOCAL_DATA_PATH + 'trees.geojson'
native_flora_file = config.LOCAL_DATA_PATH + 'native_flora.html'
urban_forest = []


def parse_arguments():
    parser = argparse.ArgumentParser(description="Options for running statistics on Sacramento's trees.")
    parser.add_argument('-f', '--fetch', action='store_true',
                        help='fetches most recent GeoJSON tree data from city website and rescrapes flora data')

    return parser.parse_args()


def fetch_geojson():
    print('Fetching GeoJSON data from', config.TREES_GEOJSON_URL, '...')
    util.requests_write_large_file(config.TREES_GEOJSON_URL, tree_file)
    print('GeoJSON saved as', tree_file)


def scrape_for_flora():
    print('Scraping', config.FLORA_URL, 'for native flora data')
    print('Downloading HTML...')
    util.requests_write_large_file(config.FLORA_URL, native_flora_file)
    print('Page has been saved as', native_flora_file)


def clean_flora_data():
    print('Cleaning up the native flora data...')
    with open(native_flora_file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    a_tags = soup.find_all(href=re.compile(config.FLORA_A_TAG_IDENTIFIER))
    flora = []
    for a in a_tags:
        flora.append(util.string_cleanup(a.get_text()))
    print('Native flora saved')


def create_forest():
    print('Creating urban forest with GEOJSON tree data...')
    with open(tree_file) as geojson_file:
        geojson_data = json.load(geojson_file)
    for feature in geojson_data['features']:
        urban_forest.append(tree.Tree(feature['properties'], feature['geometry']))
    print('Urban forest created')


def main(args):
    if args.fetch:
        fetch_geojson()
        scrape_for_flora()
    create_forest()
    clean_flora_data()


if __name__ == '__main__':
    args = parse_arguments()
    main(args)
