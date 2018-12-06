import requests


def requests_write_large_file(url, filename):
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


def string_cleanup(string):
    return string.strip().replace('.', '').lower()
