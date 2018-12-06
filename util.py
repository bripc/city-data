import requests
import bisect


def requests_write_large_file(url, filename):
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


def string_cleanup(string):
    return string.strip().replace('.', '').lower()


def binary_search(array, value):
    """ Locate the leftmost value exactly equal to value """
    i = bisect.bisect_left(array, value)
    if i != len(array) and array[i] == value:
        return array[i]
    return None
