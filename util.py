''' file with common functions to use across the application that don't belong in a class '''

# lib imports
import requests
import bisect


# requests library can't write large files all in one go, must be done in chunks.
# borrowed from StackOverflow: https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
def requests_write_large_file(url, filename):
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


# to better compare trees to scientific names
def string_cleanup(string):
    return string.strip().replace('.', '').lower()


# borrowed from PyDocs: https://docs.python.org/3/library/bisect.html#searching-sorted-lists
def binary_search(array, value):
    """ Locate the leftmost value exactly equal to value """
    i = bisect.bisect_left(array, value)
    if i != len(array) and array[i] == value:
        return array[i]
    return None
