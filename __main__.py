import argparse
import requests

# local imports
import config


def parse_arguments():
    parser = argparse.ArgumentParser(description="Options for running statistics on Sacramento's trees.")
    parser.add_argument('-f', '--fetch', action='store_true',
                        help='fetches most recent GeoJSON tree data from city website')

    return parser.parse_args()


def fetch_geojson():
    print('Fetching GeoJSON data...')
    r = requests.get(config.TREES_GEOJSON_URL, stream=True)
    print('Saving to', config.LOCAL_DATA_PATH)
    with open(config.LOCAL_DATA_PATH + 'trees.geojson', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print('GeoJSON saved as trees.geojson')


def main(args):
    if args.fetch:
        fetch_geojson()


if __name__ == '__main__':
    args = parse_arguments()
    main(args)
