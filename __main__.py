import argparse
import requests
import json

# local imports
import config
import tree

# global vars
tree_file = config.LOCAL_DATA_PATH + 'trees.geojson'
urban_forest = []


def parse_arguments():
    parser = argparse.ArgumentParser(description="Options for running statistics on Sacramento's trees.")
    parser.add_argument('-f', '--fetch', action='store_true',
                        help='fetches most recent GeoJSON tree data from city website and rescrapes flora data')

    return parser.parse_args()


def fetch_geojson():
    print('Fetching GeoJSON data...')
    r = requests.get(config.TREES_GEOJSON_URL, stream=True)
    print('Saving to', config.LOCAL_DATA_PATH)
    with open(tree_file, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print('GeoJSON saved as trees.geojson')


def scrape_for_flora():
    print('Scraping', config.FLORA_URL, 'for native tree data')
    # scrape for data here


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


if __name__ == '__main__':
    args = parse_arguments()
    main(args)
